import os
import sys
from flask import Flask, request, abort, jsonify
from models import setup_db, Actor, Movie
from flask_cors import CORS


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/movies', methods=['GET'])
    def get_movies():
        try:
            movies = [movie.format() for movie in Movie.query.all()]
            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': len(movies)
            })
        except:
            print(sys.exc_info())
            abort(404)

    @app.route('/movies', methods=['POST'])
    def create_movie():
        body = request.get_json(force=True)

        title = body.get('title', None)
        release_date = body.get('release_date', None)

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

        except:
            print(sys.exc_info())
            abort(405)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movie(movie_id):
        body = request.get_json(force=True)

        title = body.get('title', None)
        release_date = body.get('release_date', None)

        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if movie:
                movie.title = title
                movie.release_date = release_date
                movie.update()
            else:
                return jsonify({
                    "success": False,
                    'error': 'Movie not found'
                }), 404

            return jsonify({
                'success': True,
                'actors': [movie.format()]
            }), 200

        except Exception:
            return jsonify({
                "success": False,
                'error': 'Error while updating movie'
            }), 500

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            if movie:
                movie.delete()
            else:
                return jsonify({
                    "success": False,
                    'error': 'Movie not found'
                }), 404

            return jsonify({
                'success': True,
                'delete': movie_id
            }), 200

        except Exception:
            return jsonify({
                "success": False,
                'error': 'Error while deleting the movie'
            }), 500

    @app.route('/actors', methods=['GET'])
    def get_actors():
        try:
            actors = [actor.format() for actor in Actor.query.all()]
            return jsonify({
                'success': True,
                'actors': actors,
                'total_actors': len(actors)
            })
        except:
            print(sys.exc_info())
            abort(404)

    @app.route('/actors', methods=['POST'])
    def create_actor():
        body = request.get_json(force=True)

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

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

        except:
            print(sys.exc_info())
            abort(405)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def update_actor(actor_id):
        body = request.get_json(force=True)

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if actor:
                actor.name = name
                actor.age = age
                actor.gender = gender
                actor.update()
            else:
                return jsonify({
                    "success": False,
                    'error': 'Actor not found'
                }), 404

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
    def delete_actor(actor_id):
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            if actor:
                actor.delete()
            else:
                return jsonify({
                    "success": False,
                    'error': 'Actor not found'
                }), 404

            return jsonify({
                'success': True,
                'delete': actor_id
            }), 200

        except Exception:
            return jsonify({
                "success": False,
                'error': 'Error while deleting the actor'
            }), 500

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
