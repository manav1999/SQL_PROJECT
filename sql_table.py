import sql_sb
import mysql.connector
from mysql.connector import errorcode

def create_tables(tables):
    cnx=sql_sb.connect_sql()
    if cnx is None:
        print("unable to execute connect_sql")
    else:
        cursor=cnx.cursor()
        sql_sb.connect_db(cursor)
        for t_names in tables:
            t_dis=tables[t_names]
            try:
                print('Creating table {}'.format(t_names),end=" ")
                cursor.execute(t_dis)
            except mysql.connector.Error as err:
                if err.err == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("table already exists.")
                else:
                    print(err.msg)
    cursor.close()
    cnx.close()            
TABLES = {}
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
    "  `QUALITY_OF_SLEEP (1-10)` INT NULL,"
    "  `OVERALL_HAPPINESS (1-10)` INT NULL,"
    " `COMMENT` VARCHAR(45) NULL,"
    " `DATE` DATE NOT NULL,"
    "PRIMARY KEY (`DATE`),"
    "UNIQUE INDEX `DATE_UNIQUE` (`DATE` ASC) VISIBLE"
    ")ENGINE=InnoDB;")
TABLES['DALITY_ROUTINE'] = (
    "CREATE TABLE IF NOT EXISTS `sqlproject`.`DAILY_ROUTINE` ("
    "`DATE` DATE NOT NULL,"
    "`HOURS_OF_SLEEP` DECIMAL(24) NULL,"
    "`CLASSES_ATTENDED (hrs)` DECIMAL(24) NULL,"
    "`FITNESS (hrs)` DECIMAL(24) NULL,"
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


create_tables(TABLES)