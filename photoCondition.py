import sys
import time
import threading
import itertools

class Spinner:
    """A terminal spinner class to show a loading animation."""
    def __init__(self, message="Processing..."):
        self.message = message
        self.spinner_symbols = itertools.cycle(["-", "/", "|", "\\"])
        self.running = False
        self.spinner_thread = None

    def _spin(self):
        """Internal method to run the animation."""
        while self.running:
            sys.stdout.write(f"\r{self.message} {next(self.spinner_symbols)}")
            sys.stdout.flush()
            time.sleep(0.1)

    def start(self):
        """Starts the spinner animation."""
        self.running = True
        self.spinner_thread = threading.Thread(target=self._spin)
        self.spinner_thread.start()

    def stop(self):
        """Stops the spinner and clears the line."""
        self.running = False
        if self.spinner_thread:
            self.spinner_thread.join()
        
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()

lightLevel = input("What is the light level: High or Low?")
co2Level = input("What is the CO2 level: High or Low?")

spinner = Spinner("Calculating...")
spinner.start()

time.sleep(2)

spinner.stop()

if (lightLevel == "High") and (co2Level == "High"):
    print("Photosynthesis is active")
elif (lightLevel == "Low") or (co2Level == "Low"):
    print("Photosynthesis is limited")
else:
    print("The condition are unclear make sure that you put a captial letter")