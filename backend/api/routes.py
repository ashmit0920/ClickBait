from fastapi import APIRouter, HTTPException
from kafka import KafkaProducer
from pymongo import MongoClient
import json
import random
import os
from dotenv import load_dotenv
from models.mab import MultiArmedBandit

load_dotenv()

router = APIRouter()

variations = ["variation1", "variation2", "variation3"]
mab = MultiArmedBandit(variations)


@router.get("/variation")
def get_variation():
    selected_variation = random.choice(variations)
    return {"variation": selected_variation}


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["ClickBait"]
collection = db["click_events"]


@router.post("/events")
async def track_event(event: dict):
    try:
        # Send event to Kafka topic "click_events"
        producer.send("click_events", event)
        producer.flush()  # Ensure all messages are sent before moving forward
        print(f"✅ Event sent to Kafka: {event}")

        # Store event in MongoDB
        collection.insert_one(event)
        print(f"✅ Event stored in MongoDB: {event}")

        return {"message": "Event sent and stored successfully!"}

    except Exception as e:
        print(f"❌ Error in /events route: {e} \nURI - {MONGO_URI}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/events")
async def get_events():
    try:
        events = list(collection.find({}, {"_id": 0}))
        return {"events": events}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
