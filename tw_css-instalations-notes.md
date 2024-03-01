
```bash
python -m pip install -r requirements.txt

venv/bin/python -m pip install -r requirements.txt

venv/bin/pip install -r requirements.txt
```

Instalar Tailwindcss

Configurar la carpeta de `static` en el archivo `settings.py`

```py
# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
```

Instalar `django-compressor` en el entorno virtual

```bash
python -m pip install django-compressor
```

Instalar `django-compressor` en Django

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',  # <---- django-compressor
]
```

Configurar `django-compressor` en el archivo `settings.py`

```py
# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
INSTALLED_APPS += ["compressor"]
STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]
COMPRESS_ENABLED = True
```

En la carpeta `static` crear la siguiente estructura de carpetas

```bash
static
└── src
    └── input.css
```

Dentro el archivo `input.css` agregar las directivas Tailwind al CSS

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Crear en el folder `templates` la siguiente estructura de carpetas

```bash
templates
├── base.html
└── pages
    └── home.html
```

Establece la configuración por defecto para el archivo package.json

```bash
npm init -y
```

En la carpeta del proyecto donde se encuentra `manage.py`

```bash
npm install -D tailwindcss
```

Ejecutando `npx tailwindcss` se puede observar todo lo que se puede hacer con Tailwindcss

```bash
➜ npx tailwindcss     

tailwindcss v3.3.3

Usage:
   tailwindcss [--input input.css] [--output output.css] [--watch] [options...] # USE IN package.json
   tailwindcss init [--full] [--postcss] [options...]

Commands:
   init [options]

Options:
   -i, --input              Input file
   -o, --output             Output file
   -w, --watch              Watch for changes and rebuild as needed
   -p, --poll               Use polling instead of filesystem events when watching
       --content            Content paths to use for removing unused classes
       --postcss            Load custom PostCSS configuration
   -m, --minify             Minify the output
   -c, --config             Path to a custom config file
       --no-autoprefixer    Disable autoprefixer
   -h, --help               Display usage information
```

Ejecutar el comando `npx tailwindcss init` para crear el archivo `tailwind.config.js`

```js
module.exports = {
  content: [
      './templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

En el archivo `package.json` se puede configurar el comando `dev` para ejecutar `tailwindcss` y se quede en ese estado de escucha


```json
{
   "scripts": {
      "dev": "tailwindcss -i ruta-a-la-carpeta/static/src/input.css -o ruta-a-la-carpeta/static/src/output.css --watch" // <---- Ejecutar el comando npm run dev
   },
   "devDependencies": {
      "tailwindcss": "^3.4.1"
   }
}
```

En una pestaña de la terminal ejecutar el comando `npm run dev` para que se quede en estado de escucha mientras que en otra pestaña ejecutar el comando `python manage.py runserver` para levantar el servidor de Django

También se puede ejecutar el siguiente comando.

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
```

Instalar Flowbite

```bash
npm install flowbite
```

En el archivo `tailwind.config.js` en la propiedad `plugins` agregar el plugin de Flowbite

```js
module.exports = {

    plugins: [
        require('flowbite/plugin')
    ]

}
```

En el archivo `tailwind.config.js` en la propiedad `content` agregar la ruta de la carpeta `node_modules/flowbite/src/**/*.html`

```js
  content: [
      './ruta-a-la-carpeta/templates/**/*.{html, js}',
      './node_modules/flowbite/**/*.js'
  ],
```

En el archivo `base.html` justo antes de cerrar la etiqueta `</body>` incluir el archivo javascript de Flowbite CDN

```html
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"
```

















