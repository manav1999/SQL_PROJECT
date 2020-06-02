import datetime
import random

'''takes input from user'''

def daily_routine():
	''' takes input from the user for table daily_routine '''
	print("DATE",datetime.date.today()) #for test purposes 
	H_S=int(input("Amount of sleep "))
	C_A=int(input("Classes Atteneded "))
	F=int(input("Workout "))
	if (H_S+C_A++F)<=24:
		weekend=lambda x : True if(x>=5) else False
		return [datetime.date.today(), H_S,C_A,F,weekend(datetime.date.today().weekday()),]
	else:
		print("Incorrect data ")
		return []

def quality_Index():
	''' takes input from the user for quality index '''
	limiter=lambda x : 1 if (x<=1) else(10 if (x>=10) else x) #limits QOS and QOH to range 1-10
	QOS=int(input("quality of sleep(1-10)"))
	QOH=int(input("happiness (1-10)"))
	co=input("Comment ")
	return [limiter(QOS),limiter(QOH),co,datetime.date.today()]

def project():
	'''takes input for project hours from user'''
	p_name=str(input("Project name ")).capitalize()

	hs=int(input("hourse spent on this project"))
	return p_name,hs;

def pid_generate(p_name):
	'''generates pid'''
	a,b=ord(p_name[0]),ord(p_name[-1])
	a=a+b+random.randint(a,b)
	if a%2==0:
		a=a+random.randint(0,a)
	else:
		a=a+random.randint(0,b)-2
	return a


