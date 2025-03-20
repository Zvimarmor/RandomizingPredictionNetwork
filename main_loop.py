import time
import sys
import subprocess

SLEEP_MINUTES = 10

while True:
    # Run the GUI application
    python_path = sys.executable
    subprocess.run([python_path, "RandomChoiceApp.py"])
    
    # Sleep before launching again
    time.sleep(SLEEP_MINUTES * 60)
