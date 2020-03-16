# Content
* [Description](#django-app-with-custom-user)
* [Endpoints](#endpoints)
    * [Get list of all users](#get-list-of-all-users)
    * [Create new user](#create-new-user)
    * [View user details](#view-user-details)
    * [Update user](#update-user)
    * [Delete user](#delete-user)
* [Download and run](#download-and-run)

# Django app with custom user
**This is a simple Django application with**

* extended user model
* custom tags
* CRUD views
* option to download records as a .csv file

## Endpoints

### Get list of all users
* `/users` - returns all users from database

### Create new user
* `/users/add` - form for creating new user

### View user details
* `/users/<int:id>` - shows detailed info about user with given id

### Update user
* `/users/edit/<int:id>` - form for updating user with given id

### Delete user
* `/users/delete/<int:id>` - confirmation for deleting user with given id

## Download and run
**To run this project on Your computer follow these steps**
* download this repository
* create virtualenvironment (run `virtualenv venv`)
* activate virtualenvironment (run `source venv/bin/activate`)
* install requirements (run `pip install -r requirements.txt` inside project repository)
* update settings.py file with your SECRET_KEY
* run `python manage.py migrate`
* run `python manage.py runserver`
