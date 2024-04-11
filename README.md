# Example project for django_htmx_live_trigger

https://github.com/paulik123/django-htmx-live-trigger


###
This example assumes you have Redis installed and running on your local machine.


### Instructions
1. Clone the project

2. Create and activate env

3.
```bash
pip install -r requirements.txt
```

4.
```python
python3 manage.py migrate
```

To see the example open two terminals.
Run the server in the first one using ```manage.py runserver```

In the second one run: 
```python
python3 manage.py create_notification <some_notification>
```

The notifications page should update automatically