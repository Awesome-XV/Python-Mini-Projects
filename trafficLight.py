x = input("Whats the car light color?")

if x == "green":
	print("Go what you waiting for")
elif x == "yellow":
	print("You could slow down and wait but I didn't say anything")
elif x == "red":
	print("Stop! You should not be going anywhere unless you want a ticket.")
else:
	print("Where are you that you don't know the traffic light colors?")

try:
	from pause_on_exit import pause_on_exit
	pause_on_exit()
except Exception:
	pass
