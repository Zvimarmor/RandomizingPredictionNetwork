import sys
import datetime
import numpy as np
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QFrame
from PyQt6.QtCore import QTimer, Qt
from pynput import keyboard
import time

# Constants
IS_SLEEPING = True 
SLEEP_MINUTES = 1

data = []  # Data storage
color1, color2 = np.random.choice(['red', 'green'], 2, replace=False)

def log_choice(choice, color,app_instance):
    """ Log the choice and save to CSV """
    hour = datetime.datetime.now().strftime('%H:%M')
    date = datetime.datetime.now().strftime('%d.%m.%Y')
    day = datetime.datetime.now().strftime('%A')
    entry = [date, hour, day, color, choice]
    data.append(entry)
    save_data()
    app_instance.close()

def save_data():
    """ Save the choices log locally """
    try:
        existing_df = pd.read_csv("choices_log.csv")
    except FileNotFoundError:
        existing_df = pd.DataFrame(columns=['Date', 'Timestamp', 'Day', 'Color', 'Choice'])
    
    new_df = pd.DataFrame(data, columns=['Date', 'Timestamp', 'Day', 'Color', 'Choice'])
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_csv("choices_log.csv", index=False)

class ChoiceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_keyboard_listener()
    
    def initUI(self):
        """ Set up the GUI """
        self.setWindowTitle("Choose Left or Right")
        self.setGeometry(300, 100, 800, 1000)
        
        main_layout = QVBoxLayout()

        # Time Display
        time_frame = QFrame(self)
        time_frame.setStyleSheet("background-color: lightgray;")
        time_layout = QVBoxLayout()
        self.label = QLabel(datetime.datetime.now().strftime('%H:%M')) 
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 72px; font-weight: bold;")
        time_layout.addWidget(self.label)
        time_frame.setLayout(time_layout)
        main_layout.addWidget(time_frame)

        # Timer to update the time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(60000)
        
        # Buttons
        button_layout = QHBoxLayout()
        btn_left = QPushButton("Left", self)
        btn_left.setStyleSheet(f"font-size: 72px; background-color: {color1}; height: 600px;")
        btn_left.clicked.connect(lambda: log_choice(0, color1, self))
        button_layout.addWidget(btn_left)
        
        btn_right = QPushButton("Right", self)
        btn_right.setStyleSheet(f"font-size: 72px; background-color: {color2}; height: 600px;")
        btn_right.clicked.connect(lambda: log_choice(1, color2, self))
        button_layout.addWidget(btn_right)
        
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
    
    def update_time(self):
        """ Update the displayed time """
        self.label.setText(datetime.datetime.now().strftime('%H:%M'))
    
    def setup_keyboard_listener(self):
        """ Listen for left/right arrow key presses """
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
    
    def on_press(self, key):
        """ Handle keyboard events """
        try:
            if key == keyboard.Key.left:
                log_choice(0, color1, self)
            elif key == keyboard.Key.right:
                log_choice(1, color2, self)
        except AttributeError:
            pass
    
    def closeEvent(self, event):
        """ Stop keyboard listener on exit """
        self.listener.stop()
        event.accept()

def main():
    """ Main function """
    app = QApplication(sys.argv)
    window = ChoiceApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
    


        

