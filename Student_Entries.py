import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Student"]

mycollection = mydb["Student_Entries"]

mydict = [{"_id": 1, "name": "Rohan", "joining": "2019"},
          {"_id": 2, "name": "Sahil", "joining": "2018"},
          {"_id": 3, "name": "Naresh", "joining": "2000"},
          {"_id": 4, "name": "Sagar", "joining": "1995"},
          {"_id": 5, "name": "Bunty", "joining": "2014"},
          {"_id": 6, "name": "Rahul", "joining": "2019"},
          {"_id": 7, "name": "Sakshi", "joining": "2019"},
          {"_id": 8, "name": "Vicky", "joining": "2017"},
          {"_id": 9, "name": "Bablu", "joining": "2018"},
          {"_id": 10, "name": "Rakesh", "joining": "2016"},
          {"_id": 11, "name": "Charlie", "joining": "2015"},
          {"_id": 12, "name": "Davinder", "joining": "2012"}
          ]
myresult=mycollection.find()
for x in myresult:
    print(x)