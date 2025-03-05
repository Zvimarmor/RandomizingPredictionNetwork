# RandomizingPredictionNetwork

A Python application that allows users to make binary choices (left/right) with a modern GUI interface. The application logs these choices along with timestamps and color information for analysis.

## Features

- Modern PyQt6-based GUI interface
- Real-time clock display
- Two large buttons for left/right choices
- Random color assignment (red/green) for each choice
- Keyboard support (left/right arrow keys)
- Automatic data logging to CSV
- REST API endpoint for data access
- Thread-safe operation

## Requirements

- Python 3.x
- PyQt6
- Flask
- NumPy
- Pandas
- pynput

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/RandomizingPredictionNetwork.git
cd RandomizingPredictionNetwork
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python RandomChoiceApp.py
```

2. Make your choice either by:
   - Clicking the left or right button with your mouse
   - Using the left or right arrow keys on your keyboard

3. The application will:
   - Log your choice with timestamp and color information
   - Save the data to `choices_log.csv`
   - Close automatically

## Data Storage

The application saves all choices to a CSV file (`choices_log.csv`) with the following columns:
- Timestamp (HH:MM:SS)
- Day of the week
- Color (red/green)
- Choice (0 for left, 1 for right)
