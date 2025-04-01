from scipy.optimize import minimize
import numpy as np


class BayesianOptimizer:
    def __init__(self, variations, db):
        self.variations = variations
        self.collection = db["bayesian_state"]

        # Load previous performance data from MongoDB or initialize new
        self.state = self.collection.find_one({"_id": "bo"})
        if self.state:
            self.performance_data = self.state["performance_data"]
        else:
            self.performance_data = {v: [] for v in variations}
            self.save_state()

    def save_state(self):
        # Save Bayesian performance data to MongoDB.
        self.collection.update_one(
            {"_id": "bo"},
            {"$set": {"performance_data": self.performance_data}},
            upsert=True
        )

    def update_performance(self, variation, reward):
        # Update performance data for Bayesian optimization.
        self.performance_data[variation].append(reward)
        self.save_state()

    def optimize(self):
        # Optimize traffic allocation for variations.
        avg_rewards = {v: np.mean(
            self.performance_data[v]) if self.performance_data[v] else 0 for v in self.variations}

        def loss(weights):
            # Minimize negative rewards to find optimal weights
            return -sum(weights[i] * avg_rewards[v] for i, v in enumerate(self.variations))

        # Initial weights for all variations
        init_weights = [1 / len(self.variations)] * len(self.variations)
        bounds = [(0, 1) for _ in self.variations]
        constraints = {"type": "eq", "fun": lambda w: sum(w) - 1}

        result = minimize(loss, init_weights, bounds=bounds,
                          constraints=constraints)
        return {self.variations[i]: result.x[i] for i in range(len(self.variations))}
