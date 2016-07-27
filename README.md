# Web Restful API

Hello welcome to this repository! I’m creating to help developers to code your own restful api. Restful it's generally used to communicate with mobile applications or web applications.

## Getting Started

**I strongly recommend** to use virtualenv, but if you don't want to use, fell free. 

**Observation: I commit my migrations, but if you want to delete, fell free too.**

SQLite connection **admin**:

	user: root
	password: root123456
	
## Prerequisities

Basically, all prerequisities will be found in requirements.txt (libraries of application), the source uses Python 2 (by default, in Linux and OSX).

## Installing

Now, let's go to run

* Install requirements:

```bash
pip install -r requirements.txt
```

* Execute migrate/migrations:

```bash
python manage makemigrations
python manage migrate
```

* Run project locally:

```bash
python manage runserver 0.0.0.0:8000
```

## How this project will work?

It's simple to understand how to use this project in base to create your own restful api's. Below, a list of explanations:

1. Inside **`urls.py`**, we've a reference to routes. Has two files named `urls.py` and our routes references `views`.

2. **`Views`** will return a result from Rest API by using a `form`.

3. **`Forms`** basically contains all the parameters with business rules and mission to validate all of them.

4. **`Serializers`** contains the fields returned by this API.

## SQLite Database

Inside the database file (db.sqlite3), has some examples of NBA Teams (thank you [Wikipedia](https://en.wikipedia.org/) and [Fox Sports](http://www.foxsports.com/)), that I used only for studies, feel free to change it.

## RESTFUL API

At the moment, only **POST** method is used to this API:

1. **`do_create_account`** (api/user/createaccount): This method will create an user account, remember that users have only a token, when user executed a login, it's necessary to use this token to get results from api (list teams). Parameters:
	+ firstname (required), type: string
	+ lastname (required), type: string
	+ email (required), type: string
	+ password (required), type: string

2. **`do_login`** (api/user/login): Execute a login return user data and token. Parameters:
	+ username (required), type: string
	+ platform type: string, valid values: ios, and and wph
	+ password (required), type: string
	+ device_identifier, type: string
```json
{
  "message": "Success to login.",
  "user": {
    "id": 4,
    "username": "brunogabriel",
    "first_name": "Bruno Gabriel",
    "last_name": "Santos",
    "email": "bruno.gsantos89@gmail.com",
    "token": "d7f8cc0ac7a56868a153e140f0a6a23351d318f7"
  },
  "success": true
}
```

3. **`list_teams`** (api/teams/list): Will return a list of NBA teams by starting in init position until sum of init plus threshould. Parameters:
	+ username (required), type: string
	+ token (required), type: string
	+ init, type: int (default = 0)
	+ threshould, type: int (default = 10)

```json
{
  "message": "Success on list teams",
  "success": true,
  "teams": [
    {
      "id": 1,
      "name": "Boston Celtics",
      "conference": "EC",
      "arena": "TD Garden",
      "foundation": "1946-06-06",
      "about_history": "The Boston Celtics ...",
      "flag": "http://www.foxsports.com/content/dam/fsdigital/fscom/global/dev/static_resources/nba/teams/retina/2.png"
    },
    {
      "id": 2,
      "name": "Brooklyn Nets",
      "conference": "EC",
      "arena": "Barclays Center",
      "foundation": "1967-01-01",
      "about_history": "The Brooklyn Nets ...",
      "flag": "http://www.foxsports.com/content/dam/fsdigital/fscom/global/dev/static_resources/nba/teams/retina/17.png"
    }
  ]
}
```

