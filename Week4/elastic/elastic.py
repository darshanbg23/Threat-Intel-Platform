from elasticsearch import Elasticsearch
import datetime

es = Elasticsearch("http://localhost:9200")

def send_log(ip, threat):
    doc = {
        "ip": ip,
        "threat": threat,
        "timestamp": datetime.datetime.utcnow()
    }
    es.index(index="soc-logs", body=doc)
