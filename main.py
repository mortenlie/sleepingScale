from misc import getLocalHour, logg, calibrate
import time

# Configuration
timeLogg = 6
timeCalibrate = 14
excelFilename = "logg.xlsx"


localHour = getLocalHour()
localHour = 6
if localHour == timeLogg:
    logg(excelFilename)
elif localHour == timeCalibrate:
    calibrate()

time.sleep(1)
