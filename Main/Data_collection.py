import time  # For tracking elapsed time
import csv  # For writing to a CSV file
import numpy as np
from pylsl import StreamInlet, resolve_byprop
import utils

class Band:
    Delta = 0
    Theta = 1
    Alpha = 2
    Beta = 3

BUFFER_LENGTH = 5
EPOCH_LENGTH = 1
OVERLAP_LENGTH = 0.8
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH
INDEX_CHANNEL = [0]

if __name__ == "__main__":

    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=2)
    if len(streams) == 0:
        raise RuntimeError('Can\'t find EEG stream.')

    print("Start acquiring data")
    inlet = StreamInlet(streams[0], max_chunklen=12)
    eeg_time_correction = inlet.time_correction()

    info = inlet.info()
    fs = int(info.nominal_srate())

    eeg_buffer = np.zeros((int(fs * BUFFER_LENGTH), 1))
    filter_state = None
    n_win_test = int(np.floor((BUFFER_LENGTH - EPOCH_LENGTH) /
                              SHIFT_LENGTH + 1))
    band_buffer = np.zeros((n_win_test, 4))

    print('Press Ctrl-C in the console to break the while loop.')

    # CSV file setup
    csv_filename = "metrics.csv"
    with open(csv_filename, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Alpha_Metric", "Beta_Metric"])

        start_time = time.time()
        try:
            while time.time() - start_time < 30:
                eeg_data, timestamp = inlet.pull_chunk(
                    timeout=1, max_samples=int(SHIFT_LENGTH * fs))

                ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]
                eeg_buffer, filter_state = utils.update_buffer(
                    eeg_buffer, ch_data, notch=True, filter_state=filter_state)

                data_epoch = utils.get_last_data(eeg_buffer, EPOCH_LENGTH * fs)
                band_powers = utils.compute_band_powers(data_epoch, fs)
                band_buffer, _ = utils.update_buffer(band_buffer,
                                                     np.asarray([band_powers]))
                smooth_band_powers = np.mean(band_buffer, axis=0)

                alpha_metric = smooth_band_powers[Band.Alpha] / smooth_band_powers[Band.Delta]
                beta_metric = smooth_band_powers[Band.Beta] / smooth_band_powers[Band.Theta]

                print('Alpha Relaxation: ', alpha_metric)
                print('Beta Concentration: ', beta_metric)

                # Write to CSV
                csv_writer.writerow([alpha_metric, beta_metric])

        except KeyboardInterrupt:
            print('Closing!')

    print(f"Metrics saved to {csv_filename}")
