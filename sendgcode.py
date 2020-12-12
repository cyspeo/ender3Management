import serial
import time
import argparse

parser = argparse.ArgumentParser(description='This is a basic gcode sender. http://crcibernetica.com')
parser.add_argument('-p','--port',help='Input USB port',required=True)
parser.add_argument('-c','--cmd',help='Gcode command',required=True)
args = parser.parse_args()

## show values ##
print ("USB Port: %s" % args.port )
print ("Gcode command: %s" % args.cmd )

# default port '/dev/ttyUSB0'
ser = serial.Serial(args.port, 115200)

ser.write("\r\n\r\n")
time.sleep(2)
ser.flushInput() 
ser.write(args.cmd+'\n')
grbl_out = ser.readline() # Wait for response with carriage return
print ' : ' + grbl_out.strip()
time.sleep(1)
ser.close()
