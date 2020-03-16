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
