const Variation1 = ({ trackClick }) => {
  return (
    <div className="p-8 bg-white shadow-md rounded-lg">
      <h1 className="text-3xl font-bold text-primary mb-4">
        Welcome to ClickBait!
      </h1>
      <p className="text-gray-600">This is Variation 1 with a clean UI.</p>
      <button
        className="mt-4 bg-blue-950 text-white px-4 py-2 rounded"
        onClick={() => trackClick("get_started", "variation1")}
      >
        Get Started
      </button>
      <button
        className="mt-4 bg-blue-950 text-white px-4 py-2 rounded"
        onClick={() => trackClick("quit", "variation1")}
      >
        Quit
      </button>
    </div>
  );
};

export default Variation1;
