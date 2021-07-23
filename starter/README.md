## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:3000/`, which is set as a proxy in the frontend configuration and the frontend is hosted at 'http://127.0.0.1:5000/'

- Authentication: This version of the application does not require authentication or API keys. 

### Installing Dependencies for Backend and Frontend

### Backend Dependencies

	1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


	2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


	3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
	```bash
	pip install -r requirements.txt
	```

	4. **Key Dependencies**
	 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

	 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

	 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


	This will install all of the required packages we selected within the `requirements.txt` file.

### Front End Dependencies

	1. **Installing Node and NPM**<br>
	This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

	2. **Installing project dependencies**<br>
	This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:
	```bash
	npm install
	```


### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "Bad request error, what are you trying to get me to do?"
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal Server Error

### Endpoints 
#### GET /questions
- General:
    - Returns a list of categories and questions.  Each question consists of a question, an answer, a difficulty level and an assigned category no.
    - Results are paginated in groups of 10. 
	
- Sample: `curl http://127.0.0.1:5000/questions`

``` {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 51
}
```

#### POST /questions
- General:
    - Creates a new question with associated answer, difficulty level and category.
	
- `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is the first letter of the Alphabet?", "answer":"a","difficulty":"1","category":"1"}'`
```
{
  "message": "Question added",
  "success": true,
  "total_questions": 52
}
}
```
#### POST /	questions/search

-  General:
	 - Searches for a question based on 'like' criteria contained in the each question.
	
- `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"capital"}'
-	
```
{
  "current_category": null,
  "questions": [
    {
      "answer": "Cardiff",
      "category": 2,
      "difficulty": 1,
      "id": 51,
      "question": "What is the capital of Wales?"
    },
    {
      "answer": "Edinburgh",
      "category": 2,
      "difficulty": 1,
      "id": 52,
      "question": "Capital of Scotland"
    },
    {
      "answer": "London",
      "category": 2,
      "difficulty": 1,
      "id": 53,
      "question": "Capital of England"
    },
    {
      "answer": "Paris",
      "category": 2,
      "difficulty": 1,
      "id": 54,
      "question": "Capital of France"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

#### DELETE /questions/{question_id}
- General:
    - Deletes the question of the given ID if it exists.
- `curl -X DELETE http://127.0.0.1:5000/questions/105'
```
{
  "deleted": 105,
  "success": true,
  "total_questions": 52
}
```

#### /categories/{category_id}/questions
- General:
	- Returns a list of questions based on a selected category id
```
- 'curl http://127.0.0.1:5000/categories/1/questions'

{
  "categories": "Science",   
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "sucess": true,
  "total_questions": 3
}
```
#### POST /quiz
- General:
    - gives the user the option of a single category or all categories and returns a random question 5 times.  Also checks to ensure that question has not already appeared
- `curl -d '{"previous_questions": [2],"quiz_category": {"type":"Geography","id": "2"}}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/quiz`
```
{
  "question": {
    "answer": "Edinburgh",
    "category": 2,
    "difficulty": 1,
    "id": 52,
    "question": "Capital of Scotland"
  },
  "success": true
}
```