from kafka import KafkaConsumer
import json
from models import mab
from models.bayesian import BayesianOptimizer
from backend.config import variations
import logging

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    "click_events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

bo = BayesianOptimizer(variations)

# Consume clickstream events and update MAB model


def consume_click_events():
    for message in consumer:
        try:
            event = message.value
            variation = event["variationName"]
            reward = 1 if event["eventType"] == "conversion" else 0

            mab.update(variation, reward)
            logging.info(f"Updated MAB for {variation} with reward: {reward}")

            bo.update_performance(variation, reward)

            optimized_weights = bo.optimize()
            logging.info(f"Optimized Traffic Weights: {optimized_weights}")

        except Exception as e:
            logging.error(f"Error processing message: {e}")
