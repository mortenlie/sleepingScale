from misc import getLocalHour, logg, calibrate
import sys
sys.path.insert(1, 'Veieceller/hx711py')
#from hx711 import HX711
import time

print('Initiating...')
# Configuration
timeLogg = 6
timeCalibrate = 14
excelFilename = "logg.xlsx"


while True:
    localHour = getLocalHour()
    localHour = 6
    if localHour == timeLogg:
        logg(excelFilename)
    elif localHour == timeCalibrate:
        calibrate()

    input("Go ahead")
    time.sleep(1)
