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
      "about_history": "The Boston Celtics (/ˈsɛltɪks/) are an American professional basketball team based in Boston, Massachusetts. The Celtics compete in the National Basketball Association (NBA) as a member club of the league's Eastern Conference Atlantic Division. Founded in 1946 and one of eight NBA teams (out of 23 total teams) to survive the league's first decade, the team is owned by Boston Basketball Partners LLC. The Celtics play their home games at the TD Garden, which they share with the National Hockey League (NHL)'s Boston Bruins. The franchise's 17 championships are the most of any NBA franchise, and account for 24.6 percent of all NBA championships since the league's founding in 1946.[2] As a percentage of championships won, the Celtics are the most successful franchise to date in the major four traditional North American professional sports leagues.[note 1]\r\n\r\nThe Celtics have played the Lakers a record 12 times in the Finals, including their most recent appearances in 2008 and 2010, where the Celtics have won nine meetings (but only two since 1980). Four Celtics (Bob Cousy, Bill Russell, Dave Cowens and Larry Bird) have won the NBA Most Valuable Player Award for an NBA record total of 10 MVP awards.[3] Their mascot 'Lucky the Leprechaun' is a nod to the team's Irish heritage and to Boston's historically large Irish population.[4]\r\n\r\nThe Celtics rose again after struggling through the 1990s to win a championship in 2008 with the help of Kevin Garnett, Paul Pierce, and Ray Allen in what was known as the new \"Big 3\" era, following the original \"Big 3\" era of the 1980s that featured Larry Bird, Kevin McHale, and Robert Parish.\r\n\r\nAfter the end of the Big 3, general manager Danny Ainge began a rebuilding process with the help of new head coach Brad Stevens, who led the Celtics to a return to the playoffs in 2015.",
      "flag": "http://www.foxsports.com/content/dam/fsdigital/fscom/global/dev/static_resources/nba/teams/retina/2.png"
    },
    {
      "id": 2,
      "name": "Brooklyn Nets",
      "conference": "EC",
      "arena": "Barclays Center",
      "foundation": "1967-01-01",
      "about_history": "The Brooklyn Nets are an American professional basketball team based in New York City. The Nets compete in the National Basketball Association (NBA) as a member club of the Atlantic Division of the Eastern Conference. The team plays its home games at the Barclays Center, located in the borough of Brooklyn. They are one of two NBA teams located in New York City; the other is the New York Knicks. The team was established in 1967 as a charter franchise of the NBA's rival league, the American Basketball Association (ABA). They were known as the New Jersey Americans during their first season, before moving to Long Island in 1968 and changing their name to the New York Nets. During this time, the Nets won two ABA championships (in 1974 and 1976). In 1976, the ABA merged with the NBA, and the Nets were absorbed into the NBA along with three other ABA teams (the San Antonio Spurs, Indiana Pacers and Denver Nuggets, all of whom remain in the league today).\r\n\r\nIn 1977, the team returned to the nearby state of New Jersey and played as the New Jersey Nets from 1977 to 2012. During this time, the Nets won two consecutive Eastern Conference championships (in the 2001–02 and 2002–03 seasons), but failed to win a league title. In the summer of 2012, the team moved to the Barclays Center, and took its current geographic name.[6]",
      "flag": "http://www.foxsports.com/content/dam/fsdigital/fscom/global/dev/static_resources/nba/teams/retina/17.png"
    }
  ]
}
```

