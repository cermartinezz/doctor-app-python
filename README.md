Small doctor app to practice Django and Django Rest Framework.


## Installation

1. Clone the repository
2. Create a virtual environment

        > `python -m venv venv`
        > `source venv/bin/activate`

3. Install the dependencies

    > `pip install -r requirements.txt`
4. Migrate the database and create a superuser

    > `python manage.py migrate`
    > `python manage.py createsuperuser`

5. Run the server
    > `python manage.py runserver`

## Modules

1. Doctor
2. Patient
3. Appointment
4. Documentation