/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {

      colors: {
        chatblack:{50: '#212121'},
        textblack:{50: '#9B9B9B'},
        textblack2:{60: '#B4B4B4'}
      }


    }
  },
  plugins: [],
}
