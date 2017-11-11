Hackathon project

What's included?
------
- [Django v1.11.7](https://docs.djangoproject.com/en/1.11/)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Graphene-Python](http://graphene-python.org/)
- Python 3.5 based [Dockerfile](https://hub.docker.com/_/python/)
- Node 8 [docker image](https://hub.docker.com/_/node/)
- [Docker compose](https://docs.docker.com/compose/)
- [Gulp](https://gulpjs.com/)
- [Sass](http://sass-lang.com/)
- [Stylus](http://stylus-lang.com/)
- [Babel](https://babeljs.io/)
- Postgresql 9.6 database
- Template structure

How to setup project?
------
1. Setup .env file according to .env.example
2. Build project `docker-compose build`
3. Run twice database container `docker-compose up -d database`
    * Enter to database bash `docker-compose run database bash`
    * Create user according to .env file `createuser --interactive -P -s`
    * Create database according to .env file `createdb <dbname> -O <username>`
    * Leave database container `exit`
4. Install node dependencies `docker-compose run frontend yarn`
5. Run backend `docker-compose run backend bash`
    * Run migrations `python manage.py migrate`
    * Leave backend container `exit`

How to run project?
------
```bash
docker-compose up
```

Project Structure
------
* **./backend/** Django web server
  * **./api/** API application
* **./frontend/** Main frontend folder
  * **./assets/** Assets folder
    * **./js/** Javascript (including ES2015 syntax)
    * **./scss/** Sass
    * **./css/** CSS
    * **./styl/** Stylus
    * **./fonts/** Fonts
    * **./images/** Images
  * **./dist/** Results folder
