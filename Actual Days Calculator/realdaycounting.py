#!/usr/bin/env python
print("You want to enter the Data in days or years?")
print("(type d for days and y for years)")
dory = input()
print("format = realdays(days or years, the days or years)")


def realdays(data):
    if dory == "days":
        years = data / 365  # days into years
        leapdays = years * 0.25  # how many leap days
        totalnod = leapdays + data  # days + leap days = total days
        mdays = totalnod - data  # diffrence in days
        lnoy = data / 365.25  # number of years in accounting leap years
        nooy = totalnod / 365  # number of only years
        nom = ((nooy % 1) * 12)  # number of months
        nod = ((nom % 1) * 30)  # number of days
        noh = ((nod % 1) * 24)  # number of hours
        nomin = ((nod % 1) * 60)  # number of minutes
        print("Number of days : ", data)
    elif dory == "years":
        nod = data * 365
        leapdays = data * 0.25
        totalnod = nod + leapdays
        mdays = totalnod - nod
        lnoy = totalnod / 365
        lnoy = data / 365.25
        nooy = totalnod / 365
        nom = ((nooy % 1) * 12)
        nod = ((nom % 1) * 30)
        noh = ((nod % 1) * 24)
        nomin = ((nod % 1) * 60)
        print("Number of years: ", data)
    print("Number of days accounting for leap year : ", round(totalnod, 2))
    print("Number of more days :", round(mdays, 2))
    print("Number of years accounting for leap year : ", round(lnoy, 2))
    print("Actual time of", round(data, 0), "days :", round(nooy, 0), "year &", round(nom, 0),
          "months &", round(nod, 0), "days &", round(noh, 0), "hours &", round(nomin, 1), "minutes")

#print("Note: This is not fully accurate as the days of the months are not taken in consideration")
