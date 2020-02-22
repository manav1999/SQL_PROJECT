import pandas as pd
import datetime

def inputw():
        ''' inputw() takes various inputs from user during execution and returns a dictonary '''
        print("DATE",datetime.date.today())
        x=int(input("Amount of sleep "))
        y=int(input("classwork "))
        z=int(input("self learning " ))
        u=int(input("classes attended "))
        if (x+y+z+u)<=24:
                q=input('Quality of sleep ')
                m=input('mood ') 
                o=bool(input("alchol/pot "))
                weekend=lambda weekend : True if (x>=5) else False
                return dict([('d', datetime.date.today()),('W', weekend(datetime.date.today().weekday())),('g1',x),('g2',q),('g3',u),('g4',z),('g5',y),('g6',m),('g7',o)])
        
        else:
                print("Incorrect data ")
                return {}
