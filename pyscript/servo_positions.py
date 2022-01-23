import pi_servo_hat
import time
import sys

myServo = pi_servo_hat.PiServoHat()
travelSpeed = .001

def moveServo(name, position):
#	if name == "aaron":
#		if postion == "home": myServo.move_servo_position(0, 105, 180)
#		if postion == "work": myServo.move_servo_position(0, 185, 180)
#		if postion == "school": myServo.move_servo_position(0, 143, 180)
#		if postion == "away": myServo.move_servo_position(0, 65, 180)
#		if postion == "grand": myServo.move_servo_position(0, 25, 180)
#	if name == "jennifer":
#		if postion == "home": myServo.move_servo_position(1 ,90, 180)
#		if postion == "work": myServo.move_servo_position(1 ,90, 180)
#		if postion == "school": myServo.move_servo_position(1 ,90, 180)
#		if postion == "away": myServo.move_servo_position(1 ,90, 180)
#		if postion == "grand": myServo.move_servo_position(1 ,90, 180)
#	if name == "savannah":
#		if postion == "home": myServo.move_servo_position(2 ,90, 180)
#		if postion == "work": myServo.move_servo_position(2 ,90, 180)
#		if postion == "school": myServo.move_servo_position(2 ,90, 180)
#		if postion == "away": myServo.move_servo_position(2 ,90, 180)
#		if postion == "grand": myServo.move_servo_position(2 ,90, 180)
#	if name == "makayla":
#		if postion == "home": myServo.move_servo_position(3 ,90, 180)
#		if postion == "work": myServo.move_servo_position(3 ,90, 180)
#		if postion == "school": myServo.move_servo_position(3 ,90, 180)
#		if postion == "away": myServo.move_servo_position(3 ,90, 180)
#		if postion == "grand": myServo.move_servo_position(3 ,90, 180)
#	if name == "presleigh":
#		if postion == "home": myServo.move_servo_position(4 ,90, 180)
#		if postion == "work": myServo.move_servo_position(4 ,90, 180)
#		if postion == "school": myServo.move_servo_position(4 ,90, 180)
#		if postion == "away": myServo.move_servo_position(4 ,90, 180)
#		if postion == "grand": myServo.move_servo_position(4 ,90, 180)

	if name == "aaron":
		servoChannel = 0
		if position == "home":
			servoPosition = 105
		if position == "work":
			servoPosition = 185
		if position == "school":
			servoPosition = 143
		if position == "away":
			servoPosition = 65
		if position == "grand":
			servoPosition = 25

	if name == "jennifer": 
		servoChannel = 1
		if position == "home": servoPosition = 105
		if position == "work": servoPosition = 185
		if position == "school": servoPosition = 143
		if position == "away": servoPosition = 65
		if position == "grand": servoPosition = 25

	if name == "savannah": 
		servoChannel = 2
		if position == "home": servoPosition = 105
		if position == "work": servoPosition = 185
		if position == "school": servoPosition = 143
		if position == "away": servoPosition = 65
		if position == "grand": servoPosition = 25

	if name == "makayla": 
		servoChannel = 3
		if position == "home": servoPosition = 105
		if position == "work": servoPosition = 185
		if position == "school": servoPosition = 143
		if position == "away": servoPosition = 65
		if position == "grand": servoPosition = 25

	if name == "presleigh": 
		servoChannel = 4
		if position == "home": servoPosition = 105
		if position == "work": servoPosition = 185
		if position == "school": servoPosition = 143
		if position == "away": servoPosition = 65
		if position == "grand": servoPosition = 25

	currentPosition = int( myServo.get_servo_position( servoChannel, 180) )

	print("Name:", name)
	print("Postion:", position)
	print("currentPostion:", currentPosition)

	if currentPosition <= servoPosition:
		for i in range(currentPosition, servoPosition):
			myServo.move_servo_position(servoChannel, i, 180)
			time.sleep(travelSpeed)

	if currentPosition > servoPosition:
		for i in range(currentPosition, servoPosition, -1):
			myServo.move_servo_position(servoChannel, i, 180)
			time.sleep(travelSpeed)


