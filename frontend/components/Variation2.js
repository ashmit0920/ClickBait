const Variation2 = ({ trackClick }) => {
  return (
    <div className="p-8 bg-yellow-300 shadow-lg rounded-lg">
      <h1 className="text-4xl font-bold text-accent mb-4">
        Explore ClickBait!
      </h1>
      <p className="text-gray-700">This is Variation 2 with vibrant colors.</p>
      <button
        className="bg-green-500 text-white px-4 py-2 rounded"
        onClick={() => trackClick("learn_more", "variation2")}
      >
        Learn More
      </button>
      <button
        className="ml-4 bg-blue-500 text-white px-4 py-2 rounded"
        onClick={() => trackClick("sign_up", "variation2")}
      >
        Sign Up
      </button>
    </div>
  );
};

export default Variation2;
