(work in progress...)

# Blog para compartir imágenes

## Description

Proyecto de blog para compartir imágenes, donde los usuarios pueden subir imágenes y compartirlas.

Las imágenes se obtienen de la página [flickr](https://flickr.com/). Cuando por fin encuentras la imagen que te gusta y la quieres compartir,
puedes hacerlo en el blog, solo tienes que copiar la URL de la imagen y pegarla en la página "de crear el post" y ponerle etiquetas(tags)
previamente establecidas. :-)

Para poder realizar lo anterior es necesario que te registres en la página, para ello solo necesitas un correo electrónico y una contraseña.

Una ves que te hayas registrado, tendrás un perfil pre-establecido con tu nombre de usuario y tu correo electrónico para modificarlo si lo deseas
y podrás ver tus publicaciones en tu perfil con cuatro opciones de filtrado.

También otros usuarios registrados podrán comentar tus publicaciones y darles "likes" 👍

Cuenta con una sección de _Categorías_ donde podrás ver los posts por las categorías que se han creado.

Cuenta con otras dos secciones _Top Posts_ y _Top Comments_ done se muestran los posts más populares, es decir, los posts con más "likes" y comentarios. ✏️

Las imágenes se mostrarán mediante un scroll infinito, es decir, cuando llegues al final de la página se cargarán más imágenes.

## Technology Stack

![](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=Django&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/Tailwind%20CSS-06B6D4.svg?style=for-the-badge&logo=Tailwind-CSS&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black)
![](https://img.shields.io/badge/htmx-3d72d7.svg?style=for-the-badge&logo=htmx&logoColor=white)
![](https://img.shields.io/badge/Hyperscript-3465a4.svg?style=for-the-badge&logo=Hyper&logoColor=white)
![](https://img.shields.io/badge/Font%20Awesome-538DD7.svg?style=for-the-badge&logo=Font-Awesome&logoColor=white)
![](https://img.shields.io/badge/Node.js-339933.svg?style=for-the-badge&logo=nodedotjs&logoColor=white)

## To-Do

- [ ] Task 1: Versionamiento
- [ ] Task 2: Dockerizar la aplicación
- [ ] Task 3: Deploy test

## Contributing

El desarrollo esta en el ambiente linux 🐧 con PostgreSQL y NodeJS

1. Fork it!
2. Crear el ambiente virtual con `python3 -m venv ~/path/to/venv`
3. Activar el ambiente virtual con `source ~/path/to/venv/bin/activate`
4. Instalar las dependencias con `pip install -r local.txt`
5. Crear el archivo `.env` con las variables de entorno necesarias

```bash
.envs # EN EL MISMO NIVEL DE DONDE ESTA EL ARCHIVO manage.py
├── .local
│   ├── .django
│   └── .postgres
└── .production
```

En el archivo `.local` se deben de agregar las siguientes variables de entorno:

```bash
DJANGO_READ_DOT_ENV_FILE=True
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=YOUR_SECRET_KEY
DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

En el archivo `.postgres` se deben de agregar las siguientes variables de entorno:

```bash
# PostgreSQL
# ------------------------------------------------------------------------------
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

Pero si no hay una base de datos PostgreSQL, se puede usar SQLite3, para ello se puede modificar el archivo `base.py` en la carpeta `settings` en el folder `config`, de la siguiente manera:

Donde este `DATABASES = {` cambiar por:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

6. Crear la base de datos con `python manage.py makemigrations`
7. Aplicar las migraciones con `python manage.py migrate`
8. Crear un superusuario con `python manage.py createsuperuser`
9. Correr el servidor con `python manage.py runserver`

Para los estilos se utiliza **Tailwindcss**, en la misma carpeta del proyecto se debe de correr el siguiente comando:

```bash
npm install
```

Correr el siguiente comando para compilar los estilos:

```bash
npm run dev
```

## Screenshots

![Home](/screenshots/home.png "Home")

![Making a post](/screenshots/make_post.png "Making a post")

![The article](/screenshots/post_comments_replies.png "The article")

![Categories](/screenshots/posts_by_category.png "Categories")

![User sign in](/screenshots/sign_in.png "User sign in")

![User sign up](/screenshots/sign_up.png "User sign up")

![User profile](/screenshots/user_profile.png "User profile")

![Edit user profile](/screenshots/user_edit_profile.png "Edit user profile")

![User menu](/screenshots/user_menu.png "User menu")

![User password reset](/screenshots/reset_password.png "User password reset")
