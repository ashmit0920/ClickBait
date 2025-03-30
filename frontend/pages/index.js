import { useEffect, useState } from "react";
import axios from "axios";
import Variation1 from "@/components/Variation1";
import Variation2 from "@/components/Variation2";
import Variation3 from "@/components/Variation3";

export default function Home() {
  const [variation, setVariation] = useState("");

  useEffect(() => {
    // Fetch the variation dynamically from FastAPI
    axios
      .get("http://localhost:8000/api/variation")
      .then((res) => {
        setVariation(res.data.variation);
      })
      .catch((err) => console.error("Error fetching variation:", err));
  }, []);

  // Sending click events to backend (FastAPI + Kafka)
  const trackClick = async (eventType, variationName) => {
    try {
      await axios.post("http://localhost:8000/api/events", {
        eventType,
        variationName,
        timestamp: new Date().toISOString(),
      });
      console.log(`Event "${eventType}" tracked successfully!`);
    } catch (error) {
      console.error("Error sending event: ", error);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      {variation === "variation1" && <Variation1 trackClick={trackClick} />}
      {variation === "variation2" && <Variation2 trackClick={trackClick} />}
      {variation === "variation3" && <Variation3 trackClick={trackClick} />}
    </div>
  );
}
