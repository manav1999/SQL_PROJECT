import pandas as pd
import insert_data as idt

df=pd.DataFrame(columns=['date','Weekend','Amount of Sleep(in hours)','Quality of sleep(0-10)','classes attended ','Time devoted to self Learning','Time devoted to class work','mood','alchol/pot'])

di=idt.inputw()
df2=pd.DataFrame([di])
df=df.append(df2)
df.to_excel("routine.xlsx")
