# task_management

This is the Task Management Backend service.

Tech Stack:
1. Python (Language)
2. Flask (Framework)
3. MySql (Database)
4. Jwt Token (Authentication)

It performs the following activities
1. Login using JWT Token
2. User can Create a new Task
3. User can Update the Task
4. User can Delete a Task

### Prerequisite
* Pycharm or similar IDE
* Python (3.8)
* Flask
* MySql
* Jwt Token
* Virtual Environment

##Getting started

### To setup virtual environment
1) Download repo.
2) Inside that repo run following
    > pip3 install virtualenv

    > python3 -m venv venv

3) To activate this virtualenv hit one of the command.
    > source venv/bin/activate

    Now run following to install dependencies
    > python -m pip install -U pip
    > pip3 install -r requirements.txt

To stop this virtualenv, just type
> deactivate

### To run project
> ./run_api.sh default

> Go to '/apidocs' for Swagger Api
> Signup The User
> Login the User with the above username and password (It will generate token) -> User is Authenticated
> Pass The Token to top right corner in (Authorize) Section -> Now the user is authorized

> Create Task with passing the data in request body
> Get Task with get Api
> Get Sorted Tasks with Sort Task Api
> Update the status of Task
> Delete The Task

### Unit-Tests
> Sign Up the User if user is not signup
> Login Through the login api, these will generate a token.
> Update token in `run_test.sh`
> ./run_test.sh


