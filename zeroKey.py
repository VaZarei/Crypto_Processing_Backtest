

import sqlalchemy
from sqlalchemy import create_engine, text
import mysql.connector




def mySqlConf(value) : 



        var = {

        "host" : "localhost",
        "user" : "root",
        "pass" : "admin123",
        "database_name" : "traderbot" ,
                                                                      
         }
        
        return var[value]

    
def database_connection() :
        
               
        database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(mySqlConf("user"), mySqlConf("pass"), 
                                                        mySqlConf("host"), mySqlConf("database_name")))

        return database_connection

def mydb():
         
  mydb = mysql.connector.connect(  
                                host= mySqlConf("host"),
                                user= mySqlConf("user"),
                                password= mySqlConf("pass"),
                                database=mySqlConf("database_name")
                                )

  return mydb

#print(type(mySqlConf("user")))

#print(connectionTest())


#print(" mydb :", mydb)
#print(" database_connection :", database_connection)