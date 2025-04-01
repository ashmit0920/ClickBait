from fastapi import FastAPI
from api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware
import threading
from kafka_utils.consumer import consume_click_events
from database import producer, client

# Start Kafka consumer in a separate thread
consumer_thread = threading.Thread(target=consume_click_events)
consumer_thread.start()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app = FastAPI(title="ClickBait API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include API routes
app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to ClickBait API!"}


@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down server... Closing database & Kafka connections.")
    client.close()
    producer.close()
