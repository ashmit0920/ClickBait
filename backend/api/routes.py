from fastapi import APIRouter, HTTPException
from models.mab import MultiArmedBandit
from models.bayesian import BayesianOptimizer
from config import variations
from database import db, collection, producer

router = APIRouter()

mab = MultiArmedBandit(variations, db)
bo = BayesianOptimizer(variations, db)


@router.get("/variation")
def get_variation():
    selected_variation = mab.select_variation()
    return {"variation": selected_variation}


@router.post("/events")
async def track_event(event: dict):
    try:
        # Send event to Kafka topic "click_events"
        producer.send("click_events", event)
        producer.flush()  # Ensure all messages are sent before moving forward
        print(f"\n✅ Event sent to Kafka: {event}")

        # Store event in MongoDB
        collection.insert_one(event)
        print(f"✅ Event stored in MongoDB: {event}")

        return {"message": "Event sent and stored successfully!"}

    except Exception as e:
        print(f"❌ Error in /events route: {e}")
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
