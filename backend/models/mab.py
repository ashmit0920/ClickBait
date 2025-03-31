import random
import numpy as np

# Multi Armed Bandit with Epsilon-Greedy


class MultiArmedBandit:
    def __init__(self, variations, epsilon=0.3):
        self.variations = variations  # List of UI variations
        self.epsilon = epsilon        # Exploration rate
        self.counts = {v: 0 for v in variations}   # Track number of pulls
        self.rewards = {v: 0 for v in variations}  # Track cumulative rewards

    def select_variation(self):
        # Select variation using epsilon-greedy strategy.
        if random.random() < self.epsilon:
            # Explore - choose a random variation
            print(f"random choice")
            return random.choice(self.variations)
        else:
            # Exploit - choose the best variation so far
            avg_rewards = {
                v: self.rewards[v] / (self.counts[v] + 1e-5) for v in self.variations}
            print("best variation")
            return max(avg_rewards, key=avg_rewards.get)

    def update(self, variation, reward):
        # Update counts and rewards for a given variation.
        self.counts[variation] += 1
        self.rewards[variation] += reward
