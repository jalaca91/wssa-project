# Python DAO (Database Access Object)
# This programe perfoms CRUD operation on the countries_db.sql database by creating functions

import mysql.connector
import dbconfig as cfg

# Define an Object class called CountryDAO
class CountriesDAO:

    # Same DAO object to interact with different tables if required
    def __init__(self):
        self.host = cfg.mysql["host"]
        self.user = cfg.mysql["user"]
        self.password = cfg.mysql["password"]
        self.database = cfg.mysql["database"]
        self.table = cfg.mysql["table"]
        self.connection = None
        self.cursor = None
    
    # Obtain a cursor to interact with the database
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
        
    # Function to create a new record
    def create(self, data):
        cursor = self.getCursor()
        sql =  f"INSERT INTO {self.table} (country,capital,continent,currency) VALUES (%s,%s,%s,%s)"
        values = [
            data["country"],
            data["capital"],
            data["continent"],
            data["currency"]
        ]
        cursor.execute(sql,values)
        
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid
              
    # Function to get all records (read)
    def getAll(self):
        cursor = self.getCursor()
        sql = f"SELECT  * FROM {self.table}"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        
        for result in results:
            resultAsDict= self.convertToDict(result)
            returnArray.append(resultAsDict)
        self.closeAll()
        return returnArray

    # Function to update existing data
    def update(self,data):
        cursor= self.getCursor()
        sql = f"UPDATE {self.table} SET country = %s, capital = %s, continent = %s, currency = %s WHERE ID = %s;"
        values = [          
            data["country"],
            data["capital"],
            data["continent"],
            data["currency"],
            data["ID"] # ID included this time to make sure you are modifying exactly the record you need to change        
        ]
        cursor.execute(sql,values)
        self.connection.commit()
        print("update done")
        self.closeAll()
        return data
    
    # Function to delete a record
    def delete(self,id):
        cursor = self.getCursor()
        sql = f"DELETE FROM {self.table} WHERE ID = %s"
        values = (id,)

        cursor.execute(sql,values)
        self.connection.commit()
        print("delete done")
        self.closeAll()

    # Function to find a specific record by id
    def findById(self,id):
        cursor = self.getCursor()
        sql = f"SELECT * FROM {self.table} WHERE ID = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)

    # Function to convert a record to a dict object
    def convertToDict(self,result):
        attributes = ["ID","country","capital","continent","currency"]
        countryDict = {}
        if result:
            for i, attribute in enumerate(attributes):
                value = result[i]
                countryDict[attribute]= value
            return countryDict

# creates a new class
countryDAO = CountriesDAO()    

if __name__== "__main__":

    print("Group of countries")