# Testing Flask Application

For this application you will be refactoring CRUD on the resouce `snacks`. It's time to add tests! Use Flask-testing to write tests for each CRUD operation. This includes writing tests for: 

- creating a snack
- reading a snack and all snacks
- updating a snack
- deleting a snack

**Bonuses**

- Write tests for 404 errors
- Write a test that ensures your edit form is prepopulated with the snack's current values
- It would be weird if a snack's `name` or `kind` were empty. Write a test to make sure that neither is an empty string. Then write the code in your application to make the test pass!