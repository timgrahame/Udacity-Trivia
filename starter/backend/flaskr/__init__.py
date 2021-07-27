import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import false
from flask_cors import CORS, cross_origin
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type,Authorization,true')
        response.headers.add(
          'Access-Control-Allow-Methods',
          'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # ----------------Paginate Questions--------------------------------------
    def paginate_questions(request, questions, num_of_questions):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * num_of_questions
        end = start + num_of_questions

        questions = [question.format() for question in questions]
        current_questions = questions[start:end]

        return current_questions

    # ------------------Get Categories----------------------------------------
    @app.route('/categories', methods=['GET'])
    def get_categories():
        try:
            categories = Category.query.all()
            formatted_categories = {category.id: category.type
                                    for category in categories}
            return jsonify({
                  'success': True,
                  'categories': formatted_categories
            })
        except Exception:
            abort(422)

    # -----------Display a list of  Questions - 10 per page-------------------
    @app.route('/questions', methods=['GET'])
    def get_questions():
        try:
            #  get paginated questions and categories
            questions = Question.query.order_by(Question.id).all()
            total_questions = len(questions)
            categories = Category.query.order_by(Category.id).all()
            #  Paginate the questions by QUESTION_PER_PAGE global variable
            current_question = paginate_questions(
              request, questions,
              QUESTIONS_PER_PAGE)
            if len(current_question) == 0:
                abort(404)
            #  create dictionary to get category type to associate with icon.
            categories_type = {}
            for category in categories:
                categories_type[category.id] = category.type
                if len(categories_type) == 0:
                    abort(404)

            return jsonify({
              'success': True,
              'questions': current_question,
              'categories': categories_type,
              'total_questions': total_questions
            })
        except Exception:
            abort(404)

    # ---------------------Delete a Questions---------------------------------
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_questions(question_id):
        # get question that matches question_ID in endpoint - delete if exists
        try:
            questions = Question.query.filter(
                Question.id == question_id).one_or_none()

            questions.delete()

            return jsonify({
              'success': True,
              'deleted': question_id,
              'total_questions': len(Question.query.all())

            })

        except Exception:
            abort(404)

    # -------------------------Create New Questions---------------------------

    @app.route('/questions', methods=['POST'])
    def create_question():

        body = request.get_json()
        try:
            new_question = body.get('question', None)
            new_answer = body.get('answer', None)
            new_difficulty = body.get('difficulty', None)
            new_category = body.get('category', None)

            if len(new_question) == 0:
                abort(422)
            if len(new_answer) == 0:
                abort(422)

            # create new question and add them to database
            question = Question(question=new_question,
                                answer=new_answer,
                                category=new_category,
                                difficulty=new_difficulty)

            question.insert()

            return jsonify({
              'success': True,
              'message': 'Question added',
              'total_questions': len(Question.query.all())
            }), 201

        except Exception:
            abort(422)

    # ----------------------Search for Questions------------------------------
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        data = request.get_json()
        if len(data) == 0:
            abort(422)
        search_term = data.get('searchTerm')
        # search for items that are like the search_term and
        # populate current_question with found questions.
        try:
            questions = Question.query.filter(
                        Question.question.ilike(
                          "%" + search_term + "%")).all()
            if len(questions) == 0:
                abort(422)

            current_question = paginate_questions(
              request, questions,
              QUESTIONS_PER_PAGE)

            return jsonify({
              'success': True,
              'questions': current_question,
              'total_questions': len(current_question),
              'current_category': None,
            })

        except Exception:
            abort(404)

    # ------------------Get Questions based on category-----------------------

    @app.route('/categories/<int:id>/questions')
    def get_questions_by_category(id):
        try:
            category = Category.query.filter_by(id=id).one_or_none()

            if category is None:
                abort(422)

            questions = Question.query.filter_by(category=id).all()

            if questions is None:
                unprocessable_entity()

            current_question = paginate_questions(
                request, questions,
                QUESTIONS_PER_PAGE)

            return jsonify({
              'success': True,
              'questions': current_question,
              'categories': category.type,
              'total_questions': len(questions)
            })
        except Exception:
            abort(404)

    # ---------------------------Play the Quiz--------------------------------

    @app.route('/quiz', methods=['POST'])
    def play_quiz_question():
        data = request.get_json()
        previous_questions = data.get('previous_questions')
        quiz_category = data.get('quiz_category')

        if quiz_category['id'] == 0:
            questions = Question.query.all()

        else:
            questions = Question.query.filter_by(
                  category=quiz_category['id']).all()

        # get random questions
        def get_question():

            return questions[random.randint(0, len(questions)-1)]

        question = get_question()

        # check that to see if chosen question id exists in previous_question
        # list and if so, get_question again.
        if question.id in previous_questions:
            question = get_question()

        return jsonify({
          'success': True,
          'question': question.format()
        })

    # ------------------------Error Handling----------------------------------

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          'success': False,
          'error': 400,
          'message': 'Bad request error, what are you trying to get me to do?'
        }), 400

    # Error handler for resource not found (404)
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          'success': False,
          'error': 404,
          'message': 'Resource not found, we searched everywhere'
        }), 404

    # Error handler for internal server error (500)
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
          'success': False,
          'error': 500,
          'message': 'An error has occured, is the server running?'
        }), 500

    # Error handler for unprocessable (422)
    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
          'success': False,
          'error': 422,
          'message': 'I am being semantic this request can not be processed'
        }), 422

    return app
