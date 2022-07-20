import pymongo
import certifi
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@ineuron.rj3em8w.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client["test"]
print(db)

coll = db["name"]
d ={
    "name" : "himanshu",
    "email" :"himanshu@ineuron.ai",
    "surname" : "balodi"
}
y = coll.insert_one(d)