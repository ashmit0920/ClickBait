import Head from "next/head";

export default function Variation3() {
  return (
    <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
      <Head>
        <title>ClickBait - Variation 3</title>
      </Head>
      <div className="p-8 bg-gray-800 shadow-lg rounded-lg">
        <h1 className="text-3xl font-bold mb-4">Welcome to ClickBait Dark Mode!</h1>
        <p className="text-gray-400">This is Variation 3 with a sleek dark theme.</p>
      </div>
    </div>
  );
}
