# IntrepEd API

![IntrepEd API](https://user-images.githubusercontent.com/48742436/71945994-9517d580-3185-11ea-85d9-e6e4ab75c23b.png)

IntrepEd API provides the backend structure for [IntrepEd](https://github.com/intreped-learning/intreped-fe) by 
providing endpoints with CRUD functionality and database storage for the necessary educational resources.

Visit IntrepEd API [here](http://intreped-api.herokuapp.com/).

## Project Work Board
- [Github Project Board](https://github.com/orgs/intreped-learning/projects/1)

## Primary Tech Stack
- Python 3.8.0
- Django 3.0
- PostgreSQL 12.1
- Django Rest Framework 3.11.0

## Contributors
- [Chris Basham](https://github.com/chrisdbasham317)
- [Tyler Schaffer](https://github.com/tschaffer1618)

## Endpoint Examples

To see examples of the endpoints provided by IntrepEd API, please 
read [this document](https://gist.github.com/tschaffer1618/61125779f44d230567c23d9098adb776).

## Database Schema

![Database Schema](https://user-images.githubusercontent.com/48742436/71946614-921de480-3187-11ea-91e1-0641a2370af3.png)

## Local Setup

1. Install Python if you do not have it installed ([Python](https://www.python.org/downloads/)).
2. Install virtual environment if you do not have it installed with `python3 -m pip install --user virtualenv`.
3. Create a new virtual environment with `python3 -m venv dir_name`.
4. Move into the directory you created and activate the virtual environment if it isn't already (`source bin/activate`).
5. Clone this repository and move into the cloned repository.
6. Install the necessary packages with `pip3 install -r requirements.txt`.
7. To run the server locally, type `python3 manage.py runserver`.
8. To run the test suite, type `python3 manage.py test`.

