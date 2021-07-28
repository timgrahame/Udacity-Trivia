# Trivia API

Trivia api is a web application that allows people to build and play a quiz using a web interface. 

The application includes questions with an associated answer, a difficulty level and an assigned category and the user interface allows the operator to:

1. Display all questions or questions grouped by category.  Paginated 10 to a page.
2. Allows new questions to be created, with an answer, a difficulty level and category assigned.
3. Search and list questions based on a 'like' search criteria.
4. Delete questions by way of clicking on an icon.
5. Play a 5 question random quiz either from all categories or from selected categories.

# Getting started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:3000/`, which is set as a proxy in the frontend configuration

- Authentication: This version of the application does not require authentication or API keys. 

## Key Dependencies
	
	 - [PostgreSql] (https://www.postgresql.org/)  PostgreSQL is a powerful, open source object-relational database.
	
	 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

	 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

	 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Installing Dependencies

	1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
	
	2. **PostgreSql** - Follow instrctions to install the latest version of PostgreSql at https://www.postgresql.org/download/.


	3. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). For Windows and Linux users, the process is as follows:
		
		 **Windows users in Bash**

		Ensure you're in the Backend folder in Bash and follow the following.

		``` bash
		Python -m venv venv
		source venv/scripts/activate
		```
		
		**Linux users in Bash**
		
		Ensure you're in the Backend folder in Bash and follow the following.
		``` bash
		Python -m venv venv
		source venv/bin/activate	
		```


	4. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
	
	```bash
	pip install -r requirements.txt
	```
	
	This will install all of the required packages included within the `requirements.txt` file.
	

	 
	 
## Database setup
	 
	5.	Start Postgres, in windows this is achieved by typing the following in a bash window:
		
		pg_ctl -d "C:\program files\postgresql\10\data" start  	substitute the number 10 for the version number of postgresql you have installed.
		
		Then restore the database using the sample questions supplied within the trivia.psql file by typing the following from the backend folder in a bash terminal window:
		
		```bash
		psql trivia < trivia.psql
		```
		
## Running the server

	6.	From within the backend start the question server, type the following in a bash terminal window:
	
		```bash
		export FLASK_APP=flaskr
		export FLASK_ENV=development
		flask run
		```

## Testing the server

	7.	A testing script is included, to run the tests you will need to create a duplicate question database.  The following describes the process to create the database and run the tests.  Please type the following from the backend and from a bash window:
			
		```bash
		dropdb trivia_test
		createdb trivia_test
		psql trivia_test < trivia.psql
		python test_flaskr.py
		```
	
## Error handling

	8.	Errors will be returned in the following json format:
	
		```json
			  {
			   'success': False,
			   'error': 404,
			   'message': 'Resource not found, we searched everywhere'
			  }
		```
	9.	The error codes currently returned are:
	
	* 400 - Bad Request Error
	* 404 - Resource not Found Error
	* 405 - Method Not Allowed
	* 500 - Internal Server Error
	* 422 - Unprocessable Error
	
##	Endpoints

	10.	The following endpoints are used within the App:
	
	** GET / categories
	-	General:
		Returns all the categories:
		
	- `curl http://127.0.0.1:5000/categories`
	``` {
	  "categories": {     
		"1": "Science",   
		"2": "Art",       
		"3": "Geography", 
		"4": "History",   
		"5": "Entertainment",
		"6": "Sports"
	  },
	  "success": true
	}	
	``` 
	
	** GET /questions
	- General:
		- Returns a list of categories and questions.  Each question consists of a question, an answer, a difficulty level and an assigned category no.
		- Results are paginated in groups of 10. 
		
	- `curl http://127.0.0.1:5000/questions`

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

	** POST /questions
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
	** POST /questions/search

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

	** DELETE /questions/{question_id}
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

	** /categories/{category_id}/questions
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
	** POST /quiz
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
	
## Authors
	- 	Udacity created the starter files for the project for the backend and the frontend.
	
	-	Tim Grahame worked the API and created the test function to integrate with the frontend.