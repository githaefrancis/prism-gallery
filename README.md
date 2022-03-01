# Prism Gallery

## Description 

A Django web application that displays photos. Photos can be filtered based on location and searched by category.

## Technologies and Tools

- Django
- Postgresql
- Python


## Setting up the project locally

1. Clone the repository
```bash
git clone git@github.com:githaefrancis/prism-gallery.git
```

2. Navigate to the project folder
```
cd PRISM-GALLERY
```

3. Create database

4. Create .env file

```
export DB_NAME=<name_of_db>

export DB_USER='db_user'

export DB_PASSWORD='db_password'
export SECRET_KEY='secret_key'


export DEBUG='False'

export DB_HOST='127.0.0.1'

export MODE='dev'

export ALLOWED_HOSTS='.localhost','.heroku.com','.127.0.0.1'

export DISABLE_COLLECTSTATIC=1

```

5. Load .env

```
source .env

```

6. Migrate models

```
python3 manage.py migrate
```

7. Run the app

```
python3 manage.py runserver

```


## Livelink

[Prism Gallery](https://prism-gallery.herokuapp.com/)

## Contact

Email: mureithigithae@gmail.com

## License

This project is under the MIT License [click here for more information](LICENSE)

&copy; 2022 Francis Githae