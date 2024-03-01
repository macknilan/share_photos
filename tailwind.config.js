/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './apps/templates/**/*.{html, js}',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
      extend: {
          fontFamily: {
              'body': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui'],
              'sans': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui'],
              'serif': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui'],
              'mono': ['Roboto Mono', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui']
          },
     },
  },
  plugins: [
      require('flowbite/plugin')
  ]
}

