import time
from openpyxl import load_workbook, Workbook


def getLocalHour():
    secEpoch = time.time()
    localTime = time.localtime(secEpoch)
    #print("tm_hour:", result.tm_hour)
    return localTime.tm_hour

def getLocalDate():
    secEpoch = time.time()
    localTime = time.localtime(secEpoch)
    localDay = localTime.tm_mday
    localMonth = localTime.tm_mon
    localYear = localTime.tm_year

    return (localDay, localMonth, localYear)


def excelWriter(date, weight, filename):
    print("Writing")
    workbook = load_workbook(filename = filename)
    sheet = workbook.active

    # Write what you want into a specific cell
    sheet["C1"] = "writing ;)"

    # Save the spreadsheet
    workbook.save(filename=filename)

    '''
    with open(filename, "w") as csvfile:

        fieldnames = ["Dato", "Vekt"]
        writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
        writer.writeheader()
        writer.writerow({fieldnames[0]: date, fieldnames[1]: weight})
    '''



def logg(filename):
    print('Logging initiated')
    #weight = measureWeight()
    weight = 80

    date = getLocalDate()
    excelWriter(date,weight,filename)


def calibrate():
    print('Calibration initiated')
