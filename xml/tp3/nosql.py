
import pymongo

NO_SQL_ADDR = 'localhost'
NO_SQL_PORT = 666
NO_SQL_DATABASE_NAME = 'dblp'

CLIENT = pymongo.MongoClient(NO_SQL_ADDR, NO_SQL_PORT)
DB = CLIENT[NO_SQL_DATABASE_NAME]

def push(data_dict):

    DB.insert(data_dict)