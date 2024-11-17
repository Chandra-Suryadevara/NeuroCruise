# **NeuroCruze: Mind-Driven Car Control using EEG and EMG**

NeuroCruze is an innovative project that leverages brainwave data (EEG) from the Muse 2 and muscle activity (EMG) from BioAmp EXG EEG to control a car. The project uses an AI model trained on EEG data to classify mental states like relaxation and alertness, enabling seamless human-machine interaction.

## **Features**
- **EEG Integration**: Reads brain activity to detect relaxation (Alpha waves) and alertness (Beta waves).
- **EMG Input**: Captures muscle signals to enhance control.
- **AI-Powered Classification**: A custom AI model trained on EEG data for precise state recognition.
- **Real-Time Streaming**: Processes signals in real-time to drive the car.

## **Getting Started**

Follow these steps to set up and run the NeuroCruze project.

### **Prerequisites**
- **Hardware**:
  - Muse 2 (for EEG data)
  - BioAmp EXG EEG (for EMG signals)
  - Arduino-compatible microcontroller
- **Software**:
  - Python 3.x
  - Jupyter Lab
  - Arduino IDE
  - Required Python libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `torch`, `muse-lsl`

### **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/neurocruze.git
   cd neurocruze
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Upload Arduino Sketch**:
   - Open `arduino/neurocruze.ino` in the Arduino IDE.
   - Upload the sketch to your Arduino-compatible board.

### **Usage Instructions**
1. **Start the Data Stream**:
   Run the Python streaming script to begin receiving EEG and EMG data:
   ```bash
   python stream.py
   ```

2. **Launch the AI Notebook**:
   Start Jupyter Lab and open the `ai.ipynb` notebook:
   ```bash
   jupyter lab
   ```
   - Follow the notebook steps to process EEG/EMG data and control the car.

3. **Control the Car**:
   Use the trained AI model to map mental states and EMG inputs to car commands in real-time.

### **File Structure**
```
neurocruze/
├── arduino/
│   └── sketch.ino     # Arduino sketch for signal communication
├── data/
│   └── eeg_emg_data.csv   # Sample data for training/testing
├── Main/
│   └── ai.ipynb           # AI training and inference notebook
├── Main/
│   └── stream.py          # EEG/EMG streaming script
└── README.md              # Project documentation
```

### **Demo Video**
*Link to video demonstrating NeuroCruze in action.*

### **Contributing**
We welcome contributions to improve NeuroCruze! Feel free to fork this repository and create a pull request.

### **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Acknowledgments**
Special thanks to the open-source community and contributors for making this project possible.
