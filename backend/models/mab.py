import random
import numpy as np

# Multi Armed Bandit with Epsilon-Greedy


class MultiArmedBandit:
    def __init__(self, variations, db, epsilon=0.3, min_exploration=5):
        self.variations = variations  # List of UI variations
        self.epsilon = epsilon        # Exploration rate
        # minimum no. of trials for each variation (to prevent skewing)
        self.min_exploration = min_exploration
        self.collection = db['MAB_state']

        # Load previous state or initialize new
        self.state = self.collection.find_one({"_id": "mab"})
        if self.state:
            self.counts = self.state["counts"]
            self.rewards = self.state["rewards"]
        else:
            self.counts = {v: 0 for v in variations}  # Track number of pulls
            # Track cumulative rewards
            self.rewards = {v: 0 for v in variations}
            self.save_state()

    def save_state(self):
        # Save MAB state to MongoDB for persistent storage (otherwise refreshed when browser is reloaded)
        self.collection.update_one(
            {"_id": "mab"},
            {"$set": {"counts": self.counts, "rewards": self.rewards}},
            upsert=True
        )
        print("\nMAB State saved to MongoDB.")

    def select_variation(self):

        for v in self.variations:
            # Force selection until minimum exploration is met
            if self.counts[v] < self.min_exploration:
                print(f"Minimum exploration enforced: selecting {v}")
                return v

        # Select variation using epsilon-greedy strategy.
        if random.random() < self.epsilon:
            # Explore - choose a random variation
            print(f"Random Choice")
            return random.choice(self.variations)
        else:
            # Exploit - choose the best variation so far
            avg_rewards = {
                v: self.rewards[v] / (self.counts[v] + 1e-5) for v in self.variations}
            print("Best Variation")
            return max(avg_rewards, key=avg_rewards.get)

    def update(self, variation, reward):
        # Update counts and rewards for a given variation.
        self.counts[variation] += 1
        self.rewards[variation] += reward
        self.save_state()
