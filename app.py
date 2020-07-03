import os
import sys
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from models import (
    setup_db,
    Actor,
    Movie
)
from flask_cors import CORS
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def get_greeting():
        greeting = "Hello!!"
        return greeting

    @app.route('/movies', methods=['GET'])
    @requires_auth('read:movies')
    def get_movies(f):
        """ Read movies
            Tested by:
            Success:
                - test_get_movies
            Error:
                - test_error_401_read_movies
        """
        try:
            movies = [movie.format() for movie in Movie.query.all()]
            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': len(movies)
            })
        except Exception:
            print(sys.exc_info())
            abort(404)

    @app.route('/movies', methods=['POST'])
    @requires_auth('create:movie')
    def create_movie(f):
        """ Create a movie
            Tested by:
            Success:
                - test_create_movie
            Error:
                - test_error_401_create_movie
                - test_error_400_create_movie
        """
        body = request.get_json(force=True)

        title = body.get('title')
        release_date = body.get('release_date')

        if title is None:
            abort(400)

        try:
            movie = Movie(title=title, release_date=release_date)
            movie.insert()
            movies = [movie.format() for movie in Movie.query.all()]

            return jsonify({
                'success': True,
                'created': movie.id,
                'movies': movies,
                'total_movies': len(movies)
            })

        except Exception:
            print(sys.exc_info())
            abort(405)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movie')
    def update_movie(f, movie_id):
        """ Update an existing movie
            Tested by:
            Success:
                - test_update_movie
            Error:
                - test_error_401_update_movie
                - test_error_400_update_movie
        """
        body = request.get_json(force=True)

        title = body.get('title')
        release_date = body.get('release_date')

        if title is None:
            abort(400)

        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if movie:
                movie.title = title
                movie.release_date = release_date
                movie.update()
            else:
                abort(404)

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            }), 200

        except Exception:
            return jsonify({
                "success": False,
                'error': 'Error while updating movie'
            }), 500

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(f, movie_id):
        """Delete an existing Movie
            Tested by:
            Success:
                - test_delete_movie
            Error:
                - test_error_401_delete_movie
                - test_error_404_delete_movie
        """
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if movie:
                movie.delete()
            else:
                abort(404)

            return jsonify({
                'success': True,
                'deleted': movie_id
            }), 200

        except Exception:
            abort(404)

    @app.route('/actors', methods=['GET'])
    @requires_auth('read:actors')
    def get_actors(f):
        """ Read actors
            Tested by:
            Success:
                - test_get_actors
            Error:
                - test_error_401_read_actors
        """
        try:
            actors = [actor.format() for actor in Actor.query.all()]
            return jsonify({
                'success': True,
                'actors': actors,
                'total_actors': len(actors)
            })
        except Exception:
            print(sys.exc_info())
            abort(404)

    @app.route('/actors', methods=['POST'])
    @requires_auth('create:actor')
    def create_actor(f):
        """ Create an actor
            Tested by:
            Success:
                - test_create_actor
            Error:
                - test_error_401_create_actor
                - test_error_400_create_actor
        """
        body = request.get_json(force=True)

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        if name is None or age is None or gender is None:
            abort(400)

        try:
            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()
            actors = [actor.format() for actor in Actor.query.all()]

            return jsonify({
                'success': True,
                'created': actor.id,
                'actors': actors,
                'total_actors': len(actors)
            })

        except Exception:
            print(sys.exc_info())
            abort(405)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actor')
    def update_actor(f, actor_id):
        """ Update an existing actor
            Tested by:
            Success:
                - test_update_actor
            Error:
                - test_error_401_update_actor
                - test_error_400_update_actor
        """
        body = request.get_json(force=True)

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        if name is None or age is None or gender is None:
            abort(400)

        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if actor:
                actor.name = name
                actor.age = age
                actor.gender = gender
                actor.update()
            else:
                abort(404)

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            }), 200

        except Exception:
            return jsonify({
                "success": False,
                'error': 'Error while updating actor'
            }), 500

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(f, actor_id):
        """Delete an existing actor
            Tested by:
            Success:
                - test_delete_actor
            Error:
                - test_error_401_delete_actor
                - test_error_404_delete_actor
        """
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if actor:
                actor.delete()
                return jsonify({
                    'success': True,
                    'deleted': actor_id
                }), 200
            else:
                abort(404)
        except Exception:
            abort(404)

    @app.errorhandler(AuthError)
    def auth_error(exception):
        response = jsonify(exception.error)
        response.status_code = exception.status_code
        return response

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(401)
    def un_authorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Server error"
        }), 500

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
