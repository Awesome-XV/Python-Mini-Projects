x = input("Whats the traffic light color?")

if x == "green":
	print("Go what you waiting for")
elif x == "yellow":
	print("You could slow down and wait.")
elif x == "red":
	print("Stop your about to run a red light.")
else:
	print("The standard colors are green, yellow, and red and this program is exiting please run it again.")

try:
	from pause_on_exit import pause_on_exit
	pause_on_exit()
except Exception:
	pass
