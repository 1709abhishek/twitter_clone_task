# twitter_clone_task
This project is done as an assignment for algoscale hiring. Django REST framework was used to proceed with this project.

# Twitter Clone
# Project Setup
The project backend has been implmented using Django-Rest-Framework and database used is RDBMS (MySQL). The code has been properly tested, and written in a generic manner. All the unit tests have been written in tests.py for each app[rest_auth and tweets].
Steps to setup the project on your machine- 
1) Create a virtual environment using command 
>         virtualenv venv -p python3
2) Activate virtual environment using command 
>         source venv/bin/activate
3) Install requirements using command
>         pip install -r requirements.txt
4) Create database in MySQL and save your database settings in local_settings.py(database, username and password)
5) Now make migrations of project using command 
>         python manage.py makemigrations && python manage.py migrate
6) Run Django server using command
>         python manage.py runserver
All ready to go !

# List of APIs and their functionalities (Note-  Except login and signup, each request requires an authentication token[TWEET {token_value}])
API | Request Body | Method | Description | Response
|---|---|---|---|---|
| [/rest_auth/signup/] | (first_name, last_name, username, password, email, contact_number(in +91 format), country_code) | POST | User Sign up  | Authentication Token
| [/rest_auth/login/] | (username, password) | POST | User Login | Authentication Token
| [/rest_auth/logout/] | No | GET | Logout User | No
| [/tweets/tweet/[Tweet_id]/] | No | GET | Retrieve Tweet Info | Tweet
| [/tweets/tweet/user/[User_id]/] | No | GET | Get list of user's tweets | [Tweets]
| [/tweets/tweet/like/[Tweet_id]/] | (is_like) | PUT |List of Liked Tweets | No
| [/rest_auth/user/[User_id]/] | No | GET | Get user's details | User


