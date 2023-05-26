date = input('Write date in this format (mm/dd/yyyy): ')
dateList = date.split('/')

monthDict = {
    "01": "January",
    "1": "January",
    "02": "Febuary",
    "2": "Febuary",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "Sepetember",
    "10": "October",
    "11": "November",
    "12": "Decemeber",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "Sepetember"
}

monthNumMax = {
    "01": "31",
    "02": "28",
    "03": "31",
    "04": "30",
    "05": "31",
    "06": "30",
    "07": "31",
    "08": "31",
    "09": "30",
    "10": "31",
    "11": "30",
    "12": "31",
    "1": "31",
    "2": "28",
    "3": "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30"
}

i=False
while i is False:
    if date.count('/') != 2:
        date = input('Please enter the correct format, which is (mm/dd/yyyy): ')
    elif int(dateList[0]) == range(1,12):
        date = input('Please us a valid number for the month. The format is (mm/dd/yyyy): ')
    elif int(dateList[1]) > int(monthNumMax[dateList[0]] or int(dateList[1]) <= 0):
        date = input('Please enter a valid number of days for the month. The format is (mm/dd/yyyy): ')
    elif len(dateList[2]) > 4:
        date = input('That year is too high. The format  is (mm/dd/yyyy): ')
    else:
        i = True


day = dateList[1]
if int(dateList[1]) == 1:
    day = dateList[1] + "st"
elif int(dateList[1]) == 2:
    day = dateList[1] + "nd"
elif int(dateList[1]) == 3:
    day = dateList[1] + "rd"
elif int(dateList[1]) == 21:
    day = dateList[1] + "st"
elif int(dateList[1]) == 22:
    day = dateList[1] + "nd"
elif int(dateList[1]) == 23:
    day = dateList[1] + "rd"
elif int(dateList[1]) == 31:
    day = dateList[1] + "rd"
else:
    day = dateList[1] + "th"
month = monthDict[dateList[0]]
year = dateList[2]

print(f'That date is the {day} of {month} in the year of {year}')