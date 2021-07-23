import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('caryn', '1234','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #test the paginate_questions definition
    def test_paginate_questions(self):
        res = self.client().get('/questions') #resource is client getting the end point.
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200) # this is a successful result
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']), 10)

    #test the get categories definition
    def test_get_categories(self):
        res = self.client().get('/categories') 
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200) # this is a successful result
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['categories']), 6)

    #test 404 error when requesting question page that doesn't exit
    def test_404_for_page_beyond_range(self):

        res = self.client().get('/questions?page=1000000', json={'rating': 12}) 
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found, we searched everywhere')

    #test 404 error when deleting non-existent question
    def test_delete_nonexistent_question(self):

        res = self.client().delete('/questions/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found, we searched everywhere')

    #test 422 error when adding question, but leave field blank
    def test_add_question(self):

        question_data = {
            'question': 'This is a question',
            'answer': 'This is an answer',
            'difficulty': 1,
            'category': '',
        }

        res = self.client().post('/questions', json=question_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Sorry, due to me being semantic this request can not be processed')        

    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()