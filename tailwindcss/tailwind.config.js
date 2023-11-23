/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../views/*html"],
    mode: "jit",
    theme: {
        extend: {
            fontFamily: {
                sans: ['Poppins', 'sans-serif'],
                serif: ['Playfair Display', 'serif'],
            },
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}

