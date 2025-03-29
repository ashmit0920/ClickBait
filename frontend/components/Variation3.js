const Variation3 = () => {
  return (
    <div className="p-8 bg-gray-800 text-white shadow-lg rounded-lg">
      <h1 className="text-3xl font-bold mb-4">Welcome to ClickBait Dark Mode!</h1>
      <p className="text-gray-400">
        This is Variation 3 with a sleek and professional dark theme.
      </p>
      <div className="mt-4">
        <input
          type="email"
          placeholder="Enter your email"
          className="p-2 rounded bg-gray-700 text-white"
        />
        <button className="ml-2 bg-primary text-white px-4 py-2 rounded">
          Subscribe
        </button>
      </div>
    </div>
  );
};

export default Variation3;
