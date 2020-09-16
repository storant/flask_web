from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
import time
import dns
from progs.logins import mongo_login

main_db='nexmo'
coll_db='txt_sent'

client = MongoClient(mongo_login(main_db))
db = client[main_db]
coll = db[coll_db]


#("date","message-id","from","to","body","price","remaining_balance") 
#hello

def table_load(time,m_id,fr,to,body,price,remaining_balance):
    dic = {"time":time,"message-id":m_id,"from":fr,"to":to,'body':body,'price':price,'remaining-balance':remaining_balance}
    x = coll.insert_one(dic)
