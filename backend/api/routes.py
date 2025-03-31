from fastapi import APIRouter, HTTPException
from kafka import KafkaProducer
from pymongo import MongoClient
import json
import random
import os
from dotenv import load_dotenv
from models.mab import MultiArmedBandit
from models.bayesian import BayesianOptimizer
from config import variations

load_dotenv()

router = APIRouter()

mab = MultiArmedBandit(variations)
bo = BayesianOptimizer(variations)


@router.get("/variation")
def get_variation():
    selected_variation = mab.select_variation()
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


@router.get("/optimize")
async def optimize_variations():
    optimized_weights = bo.optimize()
    return {"optimized_weights": optimized_weights}
