# SimpleBudget
SimpleBudget is a budgeting site built on [Django](https://www.djangoproject.com)and [React](https://reactjs.org). It 
also uses the [Django Rest Framework](https://www.django-rest-framework.org) for the API. Currently, it is under 
development. There is no guarantee that it will work as expected.

The front end is currently under development, and is not, at the moment, present in this repository.
## Installation
First, clone the repository:
```
git clone https://github.com/speratus/SimpleBudget.git
```
Then, create a new virtual environment using whatever environment
manager you prefer.
```
virtualenv venv     #Or you can use venv
```
Once the virtual environment is setup, activate it, and execute the 
following command to install the required dependencies:
```
pip install -r requirements.txt
```
Once pip is finished installing the dependencies, you should be ready
to go.
## Running
Start the Django development server with this command:
```
python manage.py runserver
```
Make sure that python is using the path variable specified by the 
virtual environment, or you may run into errors.