# connections to mysql and mongodb
# calculate bmi
# write to mongodb

# Path: analitics/app.py
from pymongo import MongoClient
import mysql.connector

# start mysql connection

mysql = mysql.connector.connect(host='54.186.3.238', user='input', password='password', database='webdata', port=3306)

mysql_cursor = mysql.cursor()
query = ("SELECT * from input_data")
mysql_cursor.execute(query)
# assigning values to variables to a list
records = mysql_cursor.fetchall()

# mysql records
print(records)


# start mongodb connection
client = MongoClient("mongodb://root:password@54.186.3.238:27017/")


# Database Name
db = client["bmi_mongo"]

# Collection Name
col = db["bmi_table"]


# mongo records
all_data = col.find()
print(all_data)

# calculate bmi


def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


mongo_name_list = [row['name'] for row in all_data]
# all the names in mongo_db
print("mongo names are:", mongo_name_list)


for record in records:
    bmi_dict = {
        "name": record[0],
        "age": record[4],
        "gender": record[3],
        "bmi": calculate_bmi(record[2], record[1])
    }
    if bmi_dict['bmi'] < 18.5:
        classification = 'underweight'
    elif bmi_dict['bmi'] >= 18.5 and bmi_dict['bmi'] < 25:
        classification = 'normal'
    elif bmi_dict['bmi'] >= 25 and bmi_dict['bmi'] < 30:
        classification = 'overweight'
    elif bmi_dict['bmi'] >= 30:
        classification = 'obese'
    bmi_dict['classification'] = classification
    print(bmi_dict)
    if bmi_dict['name'] in mongo_name_list:
        print("name already exists")
    else:
        print("name not exists")
        col.insert_one(bmi_dict)

# closing mysql connection
mysql.close()
