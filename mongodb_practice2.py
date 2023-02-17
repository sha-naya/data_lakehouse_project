import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://ashkenov_a:Yonsei7991@cs779.4yjspoh.mongodb.net/?retryWrites=true&w=majority"
    )
db = client.test
print(db)
