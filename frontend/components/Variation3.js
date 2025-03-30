const Variation3 = ({ trackClick }) => {
  return (
    <div className="p-8 bg-gray-800 text-white shadow-lg rounded-lg">
      <h1 className="text-3xl font-bold mb-4">Welcome to ClickBait Dark Mode!</h1>
      <p className="text-gray-400">This is Variation 3 with a sleek dark theme.</p>
      <button
        className="mt-4 bg-primary text-white px-4 py-2 rounded"
        onClick={() => trackClick("subscribe", "variation3")}
      >
        Subscribe Now
      </button>
    </div>
  );
};

export default Variation3;
