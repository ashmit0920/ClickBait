import Head from "next/head";

export default function Variation2() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
      <Head>
        <title>ClickBait - Variation 2</title>
      </Head>
      <div className="p-8 bg-white shadow-lg rounded-lg">
        <h1 className="text-4xl font-bold text-accent mb-4">
          Explore ClickBait Magic!
        </h1>
        <p className="text-gray-700">This is Variation 2 with vibrant colors!</p>
      </div>
    </div>
  );
}
