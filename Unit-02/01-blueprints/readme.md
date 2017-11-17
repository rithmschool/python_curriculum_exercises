# Blueprints 

### Part I - Questions

1. Describe the MVC pattern.
2. In the MVC pattern, does the model communicate directly with the view?
2. What is the purpose of blueprints?
3. How does using blueprints help us organize bigger applications?

### Part II - Exercise

1. Refactor your users and messages app to use blueprints.  Make sure to have a separate file for `models.py`, `views.py`, and `forms.py`. You should have a working 1 to Many application with blueprints when this exercise is complete!

2. Include the following flash messages (it's important you make sure these are exact so the tests will pass)
    - when a user is created, send a flash message of "User Created!"
    - when a user is updated, send a flash message of "User Updated!"
    - when a user is deleted, send a flash message of "User Deleted!"
    - when a message is created, send a flash message of "Message Created!"
    - when a message is updated, send a flash message of "Message Updated!"
    - when a message is deleted, send a flash message of "Message Deleted!"

3. If you have not added any styling or testing to your users and messages app, be sure to do so!
