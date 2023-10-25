/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../views/*html"],
    mode: "jit",
    theme: {
        extend: {
            fontFamily: {
                'poppins': ['Poppins', 'sans'],
                'playfair-display': ['Playfair Display', 'serif']
            },
        },
    },
    plugins: [],
}

