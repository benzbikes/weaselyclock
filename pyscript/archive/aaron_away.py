import sys
import servo_positions

scriptName = sys.argv[0]

personWithPath = scriptName.split("_")[0]
person = personWithPath.rsplit("/",1)[1]
position = scriptName.split("_")[1].split(".")[0]

#print("Path:",scriptName)
#print("Person:", person)
#print("Position:", position)

servo_positions.moveServo( person, position)

