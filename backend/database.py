import os
from dotenv import load_dotenv
from pymongo import MongoClient
from kafka import KafkaProducer
import json

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["ClickBait"]
collection = db["click_events"]

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)
