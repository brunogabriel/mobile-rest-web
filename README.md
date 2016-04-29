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