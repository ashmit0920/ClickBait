const config = {
  plugins: ["@tailwindcss/postcss"],
  content: ["./pages/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#4F46E5",
        secondary: "#EC4899",
        accent: "#22C55E",
      },
    },
  },
};

export default config;
