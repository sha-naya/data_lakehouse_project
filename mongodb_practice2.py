import pymongo
import configparser

config = configparser.ConfigParser()
config.read("/Users/ayan/Desktop/BU/Spring 2023/cs779_keys.ini")



client = pymongo.MongoClient(
    host=f"mongodb+srv://{config['mongodb']['database_user']}:{config['mongodb']['database_password']}@cs779.4yjspoh.mongodb.net/?retryWrites=true&w=majority",
    )
db = client.test
print(db)
