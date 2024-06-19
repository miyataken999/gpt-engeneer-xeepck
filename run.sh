#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Run the Django application
python manage.py runserver
