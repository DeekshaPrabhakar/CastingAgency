
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}@{}/{}".format(
            'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'Tom Hanks',
            'age': 63,
            'gender': 'Male'
        }

        self.new_movie = {
            'title': 'The Da Vinci Code',
            'release_date': 'May 19, 2006'
        }

        self.assistantToken = os.environ['ASSISTANT']
        self.directorToken = os.environ['DIRECTOR']
        self.producerToken = os.environ['PRODUCER']

    # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        res = self.client().get(
            '/actors', headers={'Authorization': "Bearer {}".format(self.assistantToken)})
        data = json.loads(res.data)

        actors = [actor.format() for actor in Actor.query.all()]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actors'], actors)
        self.assertEqual(data['total_actors'], len(actors))

    def test_get_actors_without_token(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'],
                         'Authorization header is expected.')

    def test_get_movies(self):
        res = self.client().get(
            '/movies', headers={'Authorization': "Bearer {}".format(self.assistantToken)})
        data = json.loads(res.data)

        movies = [movie.format() for movie in Movie.query.all()]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], movies)
        self.assertEqual(data['total_movies'], len(movies))

    def test_get_movies_without_token(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'],
                         'Authorization header is expected.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
