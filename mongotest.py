import pymongo

client = pymongo.MongoClient("mongodb+srv://ammukwfp:<password>@cluster0.z8gfymp.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)
d = {"name":"ammukwfp", "email":"amruthrajaras@gmail.com", "last_name":"kumar"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

