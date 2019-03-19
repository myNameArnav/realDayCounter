#!/usr/bin/env python

def realdays(x):
	noy = x / 365					#days into years
	leapdays = noy * 0.25			#how many leap days
	totalnod = leapdays + x			#days + leap days = total days
	mdays = totalnod - x	 		#diffrence in days
	lnoy = x / 365.25				#number of years in accounting leap years
	nooy = totalnod / 365 			#number of only years
	nom = ((nooy % 1) * 12)			#number of months
	nod = ((nom % 1) * 30)			#number of days
	noh = ((nod % 1) * 24)			#number of hours
	nomin = ((nod % 1)* 60)			#number of minutes



	print("Number of days : ", x)
	print("Number of days accounting for leap year : ", round(totalnod,2))
	print("Number of more days :", round(mdays,4))
	print("Actual time of",round(x,0), "days :" , round(nooy,0), "year &", round(nom,0), "months &", round(nod,0), "days &", round(noh,0), "hours &", round(nomin,1), "minutes")


'''
print ("How many Days/Years?(D for Days/Y for Years)")
selection = input()

if selection == "d":
	print("How many Days?")
	days = float(input())
	noy = days / 365				#days into years
	leapdays = noy * 0.25			#how many leap days
	totalnod = leapdays + days		#days + leap days = total days
	mdays = totalnod - days 		#diffrence in days
	lnoy = days / 365.25			#number of years in accounting leap years
	nooy = totalnod / 365 			#number of only years
	nom = ((nooy % 1) * 12)			#number of months
	nod = ((nom % 1) * 30)			#number of days
	noh = ((nod % 1) * 24)			#number of hours
	nomin = ((nod % 1)* 60)			#number of minutes
	#----------Print-----------
	print("Number of days : ", days)
	print("Number of days accounting for leap year : ", round(totalnod,2))
	print("Number of more days :", round(mdays,4))
	print("Actual time of",round(days,-1), "days :" , round(nooy,0), "year &", round(nom,0), "months &", round(nod,0), "days &", round(noh,0), "hours &", round(nomin,1), "minutes")
if selection == "y":
	print("How many Years?")
	years = float(input())
	nod = years * 365
	leapdays = years * 0.25
	totalnod = nod + leapdays
	mdays = totalnod - nod
	lnoy = totalnod / 365
	#----------Print-----------
	print("Number of years: ", years)
	print("Number of days : ", nod)
	print("Number of days accounting for leap year : ", round(totalnod,2))
	print("Number of more days :", round(mdays,2))
	print("Number of years accounting for leap year : ", round(lnoy,2))




print("Note: This is not fully accurate as the days of the months are not taken in consideration")
#	1 year = 12 months = 52 weeks = 365.25 days
'''
