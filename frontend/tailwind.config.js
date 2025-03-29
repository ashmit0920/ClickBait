/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./pages/**/*.{js,ts,jsx,tsx}", // Include all pages
      "./components/**/*.{js,ts,jsx,tsx}", // Include all components
    ],
    theme: {
      extend: {
        colors: {
          primary: "#4F46E5",
          secondary: "#EC4899",
          accent: "#22C55E",
        },
      },
    },
    plugins: [],
  };
  