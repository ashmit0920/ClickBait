import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [variation, setVariation] = useState("");

  useEffect(() => {
    // Fetch the variation dynamically from FastAPI
    axios
      .get("http://localhost:8000/variation") // Ensure FastAPI is running on port 8000
      .then((res) => {
        setVariation(res.data.variation);
      })
      .catch((err) => console.error("Error fetching variation:", err));
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center">
      {variation === "variation1" && (
        <div className="p-8 bg-white shadow-md rounded-lg">
          <h1 className="text-3xl font-bold text-primary mb-4">
            Welcome to ClickBait!
          </h1>
          <p className="text-gray-600">This is Variation 1 of the UI.</p>
        </div>
      )}
      {variation === "variation2" && (
        <div className="p-8 bg-white shadow-lg rounded-lg">
          <h1 className="text-4xl font-bold text-accent mb-4">
            Explore ClickBait Magic!
          </h1>
          <p className="text-gray-700">This is Variation 2 with vibrant colors!</p>
        </div>
      )}
      {variation === "variation3" && (
        <div className="p-8 bg-gray-800 text-white shadow-lg rounded-lg">
          <h1 className="text-3xl font-bold mb-4">Welcome to ClickBait Dark Mode!</h1>
          <p className="text-gray-400">This is Variation 3 with a sleek dark theme.</p>
        </div>
      )}
    </div>
  );
}
