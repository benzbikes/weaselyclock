import pi_servo_hat
import time
import sys

myServo = pi_servo_hat.PiServoHat()
travelSpeed = .001
n = len(sys.argv)

if n == 3:
	name = sys.argv[1]
	location = sys.argv[2]

	if name == "aaron":
		servoChannel = 0
		if location == "home": servoPosition = 105
		if location == "work": servoPosition = 185
		if location == "school": servoPosition = 143
		if location == "away": servoPosition = 65
		if location == "grand":	servoPosition = 25

	if name == "jennifer": 
		servoChannel = 1
		if location == "home": servoPosition = 105
		if location == "work": servoPosition = 185
		if location == "school": servoPosition = 143
		if location == "away": servoPosition = 65
		if location == "grand": servoPosition = 25

	if name == "savanna": 
		servoChannel = 2
		if location == "home": servoPosition = 105
		if location == "work": servoPosition = 185
		if location == "school": servoPosition = 143
		if location == "away": servoPosition = 65
		if location == "grand": servoPosition = 25

	if name == "makayla": 
		servoChannel = 3
		if location == "home": servoPosition = 105
		if location == "work": servoPosition = 185
		if location == "school": servoPosition = 143
		if location == "away": servoPosition = 65
		if location == "grand": servoPosition = 25

	if name == "presleigh": 
		servoChannel = 4
		if location == "home": servoPosition = 105
		if location == "work": servoPosition = 185
		if location == "school": servoPosition = 143
		if location == "away": servoPosition = 65
		if location == "grand": servoPosition = 25

	currentPosition = int( myServo.get_servo_position( servoChannel, 180) )

	print("Name:", name)
	print("Location:", location)
	print("currentPostion:", currentPosition)

	if currentPosition <= servoPosition:
		for i in range(currentPosition, servoPosition):
			myServo.move_servo_position(servoChannel, i, 180)
			time.sleep(travelSpeed)

	if currentPosition > servoPosition:
		for i in range(currentPosition, servoPosition, -1):
			myServo.move_servo_position(servoChannel, i, 180)
			time.sleep(travelSpeed)

if n == 1:
	for i in range(-100, 280):
		for n in range(0 , 4):
			myServo.move_servo_position(n, i, 180)
			time.sleep(travelSpeed / 5)
	for i in range(280, -100, -1):
		for n in range(0, 4):
			myServo.move_servo_position(n, i, 180)
			time.sleep(travelSpeed /5)
