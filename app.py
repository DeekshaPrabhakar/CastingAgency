import os
import sys
from flask import Flask, request, abort, jsonify
from models import setup_db, Actor, Movie
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
        body = request.get_json(force=True)

        title = body.get('title', None)
        release_date = body.get('release_date', None)

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
        body = request.get_json(force=True)

        title = body.get('title', None)
        release_date = body.get('release_date', None)

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
        body = request.get_json(force=True)

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

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
        body = request.get_json(force=True)

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

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
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(404)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
