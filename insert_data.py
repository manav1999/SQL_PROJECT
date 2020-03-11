import pandas as pd
import datetime

def daily_routine():
	''' takes input from the user for table daily_routine '''
	print("DATE",datetime.date.today()) #for test purposes 
	H_S=int(input("Amount of sleep "))
	C_A=int(input("Classes Atteneded "))
	F=int(input("Fitness"))
	if (H_S+C_A++F)<=24:
		weekend=lambda x : True if(x>=5) else False
		return [datetime.date.today(), weekend(datetime.date.today().weekday()),H_S,C_A,F]
	else:
		print("Incorrect data ")
		return {}

def quality_Index():
	''' takes input from the user for quality index '''
	limiter=lambda x : 1 if (x<=1) else(10 if (x>=10) else x) #limits QOS and QOH to range 1-10
	QOS=int(input("quality of sleep(1-10)"))
	QOH=int(input("happiness (1-10)"))
	co=input("Comment ")
	return [limiter(QOS),limiter(QOH),co]

def project():
	'''takes input for project hours from user'''
	 p_id = int(input("project"))
	 p_name=input("Project name ")
	 hs=int(input("hourse spent on this project"))
	 return [p_id,p_name,hs]







