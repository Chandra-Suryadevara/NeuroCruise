import time
import numpy as np
from muselsl import stream, list_muses, view
from pylsl import StreamInlet, resolve_byprop
import matplotlib.pyplot as plt
from collections import deque

# Parameters for real-time visualization
BUFFER_SIZE = 256  # Buffer size for data (in samples)
CHANNELS = ['TP9', 'AF7', 'AF8', 'TP10']  # Muse 4 default channels
PLOT_WINDOW = 2  # Plot data for the last 2 seconds

# Function to update the plot
def update_plot(lines, buffer, data):
    buffer.extend(data)
    while len(buffer) > BUFFER_SIZE:
        buffer.popleft()
    for i, line in enumerate(lines):
        line.set_ydata(buffer)
    return lines

def main():
    # List available Muse devices
    muses = list_muses()
    if not muses:
        print("No Muse device found. Please connect and try again.")
        return

    # Start streaming from the first Muse device
    print(f"Connecting to Muse: {muses[0]['name']}...")

    print(f"{muses[0]['address']}")
    stream(muses[0]['address'])


if __name__ == "__main__":
    main()
