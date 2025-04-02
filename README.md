<div align="center">
    <h1>
    ClickBait <img src="./click.gif" width="40px">
    </h1>
    <p>
    But the smart kind<br>
    </p>
    <p></p>
</div>

In traditional A/B testing, UI/UX variations are tested manually over a predefined period, and decisions are made based on post-hoc analysis. This process is:

- **Slow and Manual:** Analysts need to monitor and interpret results manually.
- **Delayed Optimization:** The best-performing variation is identified only after a lot of data has been collected.
- **Static Models:** UI/UX variations do not adapt dynamically to user behavior.

---

### ClickBait is a Clickstream-Based Dynamic A/B Testing Engine that:

- **Collects Clickstream Data:** Tracks user interactions (clicks, scrolls, conversions) on different UI/UX variations.

- **Analyzes Conversion Metrics:** Monitors key metrics such as bounce rates, dwell time, and CTRs (Click-Through Rates).

- **Dynamically Selects the Winning Variation:** Uses a **Multi-Armed Bandit (MAB)** (Explore-Exploit approach) and **Bayesian Optimization** algorithm to identify and prioritize high-performing variations.

- **Automates Experiment Results:** Displays real-time A/B testing insights on a dashboard.

- **Triggers UI Changes in Real-Time:** Automatically adjusts the UI for future users based on winning variations.

---

## ✅ Use Cases:

- E-commerce websites optimizing landing pages.
- SaaS platforms testing different onboarding flows.
- News/media sites recommending personalized content.

## 🛠️ Tech Stack

#### 🧩 **Backend:**
- **FastAPI:** API to handle incoming clickstream data and serve results.
- **Apache Kafka:** Stream, store and distribute real-time clickstream data to different microservices.

#### 🎨 **Frontend:**
- **Next.js:** UI to display different A/B variations and dynamically update content.
- **WebSocket / REST API:** Trigger UI updates based on winning variations.

#### 🧠 **ML Algorithms:**
- **Multi-Armed Bandit (MAB):** Dynamic exploration-exploitation to test and optimize variations.
- **Bayesian Optimization:** Identify high-performing UI elements with probabilistic models.
- **Upper Confidence Bound (UCB):** (Coming Soon)

#### 📦 **Database:**
- **MongoDB:** Store clickstream data, variation performance, and user activity.
- **Redis:** For caching real-time analytics and persistent MAB/BO states.

#### 📊 **Visualization & Insights:**
- **Grafana:** Real-time A/B test result visualization.

#### 🚀 **Deployment:**
- **Docker:** Containerized backend, frontend, and model services.
- **AWS:** (Coming soon)

## How to Run

1. Create a .env file in the root directory and add your MongoDB connection string to it:

```
MONGO_URI = "YOUR_CONNECTION_STRING"
```

2. Run the Back-end using uvicorn:

```
ClickBait\backend> uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

3. Run the Front-end:

```
ClickBait\frontend> npm run dev
```

4. Build and run Apache Kafka and Zookeeper using Docker:

```
ClickBait> docker-compose up -d
```
You can check if the containers are running properly using `docker-compose ps`.

## Customisation for your own UIs

1. Add variations of your user interfaces in the `ClickBait/frontend/components` directory. Make sure that all the buttons (that needs to be tracked) send out a click event, using the `trackClick(eventType, variationName)` method.

2. Define the list of variations, and buttons/events that have a positive "reward" in the `ClickBait/backend/config.py` file. All other clicks/events that aren't defined here would be assigned a reward of -1. If not configured correctly, the MAB and Bayesian Optimizers would fail and produce incorrect results.

3. For debugging purposes, each click/event is logged and also stored in MongoDB, and details for each variation (such as MAB status updates, Optimized traffic weights, etc) is continuously printed in the uvicorn terminal after each event.