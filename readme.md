Description
===========

This project aims to manage users and their bank account data (IBAN).

Requirements
============

- Docker 1.13.0 or higher
- docker-compose 1.22.0 or higher

Installation steps
==================

- Remove `template` extension from `env_file.template`
- Fill the `env_file` with the following content:
    * GOOGLE_CLIENT_ID: The client id of google sign-in. More info [here](https://developers.google.com/identity/sign-in/web/sign-in)
    * POSTGRES_DB: The name of the database that postgres will create.
    * POSTGRES_USER: The database user that postgres will create
    * POSTGRES_PASSWORD: The database user password
    * SECRET_KEY: The secret key that django will use
    * DEBUG_MODE: put `True` if you want to run the app in the debug mode, `False` otherwise
- run `docker-compose up -d`