create database if not exists traderbot ;
use traderbot ;



 print(" frame :", frame)

        mycursor = mydb.cursor()

        query = """
                create database if not exists traderbot ;
                use traderbot ;

                """
        mycursor.execute(query, multi=True)
        mydb.commit()

# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# update table 

mycursor = mydb.cursor()
query = "update adausd_1d set Date = '11-01-11' where Date='2023-02-28' ; "
mycursor.execute(query)
mydb.commit()

# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# Create or insert  to table 

mycursor = mydb.cursor()
query = "INSERT INTO adausd_1d (Date, Volume) VALUES (%s , %s)"   # Edit on 1d timeframe
val = ["2024-01-01" , "254789"]
mycursor.execute(query, val)
mydb.commit()

# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# Delete from table

mycursor = mydb.cursor()            
query = " delete from adausd_1d where Date='2023-02-26';"
mycursor.execute(query)
mydb.commit()
# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------
# Read or select from table

query1 = text("select * from {table_name} where Date > '2023-02-01 12:45:00' ; ".format(table_name=table_name))     
query1 = text("select * from {table_name}  ; ".format(table_name=table_name))     

df = pd.read_sql(query1, database_connection().connect())
print(df)
# ---------------------------------- ---------------------------------- ---------------------------------- ---------------------------------- ----------------------------------

