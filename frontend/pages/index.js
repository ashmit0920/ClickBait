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

  return (
    <div className="min-h-screen flex items-center justify-center">
      {variation === "variation1" && <Variation1 />}
      {variation === "variation2" && <Variation2 />}
      {variation === "variation3" && <Variation3 />}
    </div>
  );
}
