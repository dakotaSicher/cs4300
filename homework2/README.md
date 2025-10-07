### Setup

1. Create a new virtual environemnt
```python -m venv venv_name```
2. Activate the virtual environemnt
``` source (path to venv)/bin/activate ```
3. Install the requirements
``` python -m pip install -r requirements.txt ```
4. Set up database
```python manage.py migrate```
5. (optional) Add test data
```python -m add_data.py```
6. Run tests
``` python manage.py tests```
7. Run Server
``` python manaage.py runserver```

### Note to instructor on AI use
Used Caude Sonnet 3.5 for creating add_data.py script
Used ChatGpt-5 for testing boilerplate
Used ChatGpt-5 for some html and css stuff to make it pretty