import random
import sys
import time
import itertools
import threading

x = input("Enter desired sum (2-12): ")
x = int(x)

if x >= 2 and x <= 12:
   ran = random.randint(1, 6)
   ran2 = random.randint(1, 6)
   print("Desired sum:", x)
else:
    x = input("Please enter a number between 2 and 12 and read the question correctly")

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

spinner = Spinner("Calculating...")
spinner.start()

time.sleep(2)

spinner.stop()

rolls = 0
while ran != x:
    ran = random.randint(1, 6)
    ran2 = random.randint(1, 6)
    total = ran + ran2
    print(ran, "and", ran2, "=", total)
    if x == total:
        break
    
