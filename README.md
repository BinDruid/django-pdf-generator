# PDF Generation Template Views For Django

Minimal django application to demo capability of building PDF files inside a
django template view via `xelatex` or `headless chrome`.

## Run Project

- Install dependencies

```sh
$ pipenv shell
$ pipenv install
```

- Migrate database

```sh
$ python manage.py migrate
```

- Run django server and visit demo urls

```sh
$ python manage.py runserver
```

`localhost:8000/latex/` or `localhost:8000/chrome/`
