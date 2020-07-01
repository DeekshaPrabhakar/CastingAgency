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

    @app.route('/actors', methods=['GET'])
    def get_actors():
        try:
            actors = Actor.query.all()
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
        body = request.get_json(force = True)

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

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
