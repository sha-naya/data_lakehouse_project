import pymongo
import configparser

config = configparser.ConfigParser()
config.read("/Users/ayan/Desktop/BU/Spring 2023/cs779_keys.ini")



client = pymongo.MongoClient(
    host=f"mongodb+srv://{config['mongodb']['database_user']}:{config['mongodb']['database_password']}@mycluster.2gvwkvc.mongodb.net/?retryWrites=true&w=majority",
    )

db = client['sample_analytics']
coll = db['transactions']
x = coll.find_one()
print(x)
