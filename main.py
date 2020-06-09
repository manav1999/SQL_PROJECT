import mysql.connector
from mysql.connector import errorcode
import sql_table
import insert_sql
import plot_data


TABLES = {} #dictonary of lis of table schema

TABLES['USER'] = (
    "CREATE TABLE IF NOT EXISTS `sqlproject`.`USER` ("
    "  `USERNAME` VARCHAR(45) NOT NULL,"
    "  `PASSWORD` VARCHAR(45) NOT NULL,"
    "  `U_ID` CHAR(5) NOT NULL,"
    "  PRIMARY KEY (`U_ID`),"
    "  UNIQUE INDEX `U_ID_UNIQUE` (`U_ID` ASC) VISIBLE,"
    "  UNIQUE INDEX `USERNAME_UNIQUE` (`USERNAME` ASC) VISIBLE"
    ") ENGINE=InnoDB;")   
TABLES['QUALITY INDEX'] = (
    "CREATE TABLE IF NOT EXISTS `sqlproject`.`QUALITY_INDEX` ("
    "  `QOS` INT NULL,"
    "  `OH` INT NULL,"
    " `COMMENT` VARCHAR(45) NULL,"
    " `DATE` DATE NOT NULL,"
    "PRIMARY KEY (`DATE`),"
    "UNIQUE INDEX `DATE_UNIQUE` (`DATE` ASC) VISIBLE"
    ")ENGINE=InnoDB;")
TABLES['DALITY_ROUTINE'] = (
    "CREATE TABLE IF NOT EXISTS `sqlproject`.`DAILY_ROUTINE` ("
    "`DATE` DATE NOT NULL,"
    "`HOURS_OF_SLEEP` DECIMAL(24) NULL,"
    "`CLASSES_ATTENDED` DECIMAL(24) NULL,"
    "`WORKOUT` DECIMAL(24) NULL,"
    "`WEEKEND` TINYINT NOT NULL,"
    "PRIMARY KEY (`DATE`),"
    "UNIQUE INDEX `DATE_UNIQUE` (`DATE` ASC) VISIBLE,"
    "CONSTRAINT `DATE` FOREIGN KEY (`DATE`) REFERENCES `sqlproject`.`QUALITY_INDEX` (`DATE`) ON DELETE NO ACTION ON UPDATE NO ACTION"
    ")ENGINE=InnoDB;")
TABLES['PROJECT'] = (
    "CREATE TABLE IF NOT EXISTS `sqlproject`.`PROJECT` ("
    "`PROJECT_ID` INT NOT NULL,"
    "`PROJECT_NAME` VARCHAR(45) NOT NULL,"
    "`HOURS_SPENT` DECIMAL(24) NULL,"
    "PRIMARY KEY (`PROJECT_ID`),"
    "UNIQUE INDEX `PROJECT_ID_UNIQUE` (`PROJECT_ID` ASC) VISIBLE"
    ")ENGINE=InnoDB;")

sql_table.create_tables(tables=TABLES)
b=True
while (b== True ):
    print("1. Enter Data, 2. Plot ")
    a=int(input("Enter your choice"))
    if a==1:
        insert_sql.daily_input()
    elif a==2:
        print("1.DATE vs Hours of sleep,2.DATE vs Classes attended,3.Date vs workout,4.Date vs Quality of sleep,5.Date vs happines,6.Projects")
        x=int(input())
        if x==1:
            plot_data.plot_DvsS()
        elif x==2:
            plot_data.plot_DvsC()
        elif x==3:
            plot_data.plot_DvsW()
        elif x==4:
            plot_data.plot_DvsQOS()
        elif x==5:
            plot_data.plot_DvsQOh()
        elif x==6:
            plot_data.pro_plot()
        else:
            print("Wrong choice")

        





    
