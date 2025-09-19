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

e = input("Whats your number grade in English? ")
m = input("Whats your number grade in Math? ")
s = input("Whats your number grade in Science? ")
h = input("Whats your number grade in History? ")
el = input("Whats your number grade in Elective? ")

spinner = Spinner("Calculating...")
spinner.start()

time.sleep(2)

try:
    e = int(e)
    m = int(m)
    s = int(s)
    h = int(h)
    el = int(el)
except ValueError:
    print("Error: Please enter a number for the grades.")
    print("Exiting...")
    spinner.stop()
else:
    percent = (e + m + s + h + el) / 5

    spinner.stop()

    print("---------Printing Result--------")
    print("Here is your percent: ", percent)

    if percent < 45:
        print("Failing you better do something")
    elif percent <= 60:
        print("passed somehow u dont deserve caps")
    elif percent <= 75:
        print("You did good (not really but try to earn caps)")
    elif percent <= 85:
        print("You did really good (maybe you deserve caps)")
    elif percent <= 100:
        print("You did exellent (You deserve caps)")
    elif (percent < 0) or (percent > 100):
        print("Error, or you either you did really good or really bad")
    else:
        print("Are you sure that you typed a number? The default is that you are failing so you're failing.")

try:
    from pause_on_exit import pause_on_exit
    pause_on_exit()
except Exception:
    pass
