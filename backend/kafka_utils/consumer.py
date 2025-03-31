from kafka import KafkaConsumer
import json
from models.mab import MultiArmedBandit
from models.bayesian import BayesianOptimizer
from config import variations

consumer = KafkaConsumer(
    "click_events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

mab = MultiArmedBandit(variations)
bo = BayesianOptimizer(variations)

# Consume clickstream events and update MAB model


def consume_click_events():
    for message in consumer:
        try:
            event = message.value
            variation = event["variationName"]

            # Defining events for which reward should be 1
            positive_events = ["get_started",
                               "learn_more", "sign_up", "subscribe"]
            reward = 1 if event["eventType"] in positive_events else 0

            mab.update(variation, reward)
            print(
                f"From consumer.py - Updated MAB for {variation} with reward: {reward}")

            bo.update_performance(variation, reward)

            optimized_weights = bo.optimize()
            print(
                f"From consumer.py - Optimized Traffic Weights: {optimized_weights}")

        except Exception as e:
            print(f"Error processing message: {e}")
