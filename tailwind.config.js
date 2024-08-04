/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "1rem",
      screens: {
        sm: "100%",
        md: "100%",
        lg: "100%",
        xl: "1280px",
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        cyan: {
          50: "#E0FCFF",
          100: "#BEF8FD",
          200: "#87EAF2",
          300: "#54D1DB",
          400: "#38BEC9",
          500: "#2CB1BC",
          600: "#14919B",
          700: "#0E7C86",
          800: "#0A6C74",
          900: "#044E54",
        },
        purple: {
          50: "#F5EFFF",
          100: "#E6D6FF",
          200: "#C4A3E8",
          300: "#A06BDE",
          400: "#7E3FDF",
          500: "#6619DB",
          600: "#550EC8",
          700: "#470DA8",
          800: "#380A8A",
          900: "#27056D",
        },
      },
      animation: {
        pulse: "pulse 2s infinite",
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
    keyframes: {
      "accordion-down": {
        from: { height: "0" },
        to: { height: "var(--radix-accordion-content-height)" },
      },
      "accordion-up": {
        from: { height: "var(--radix-accordion-content-height)" },
        to: { height: "0" },
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};
