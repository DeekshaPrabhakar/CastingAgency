
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
from datetime import datetime


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
            'age': 61,
            'gender': 'Male'
        }

        self.update_actor_valid = {
            'name': 'Tom Hanks',
            'age': 63,
            'gender': 'Male'
        }

        self.invalid_actor = {
            "title": "Tom Hanks"
        }

        self.new_movie = {
            'title': 'The Da Vinci Code',
            'release_date': datetime.strptime('2006-5-5', '%Y-%m-%d')
        }

        self.update_movie_valid = {
            'title': 'The Da Vinci Code',
            'release_date': datetime.strptime('2003-3-18', '%Y-%m-%d')
        }

        self.invalid_movie = {
            'name': 'Tom Hanks'
        }

        self.assistantToken = os.environ['ASSISTANT']
        self.directorToken = os.environ['DIRECTOR']
        self.producerToken = os.environ['PRODUCER']
        self.assistantHeader = {
            'Authorization': "Bearer {}".format(self.assistantToken)}
        self.directorHeader = {
            'Authorization': "Bearer {}".format(self.directorToken)}
        self.producerHeader = {
            'Authorization': "Bearer {}".format(self.producerToken)}

    # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        movies = Movie.query.filter(Movie.title == 'The Da Vinci Code').all()
        for movie in movies:
            movie.delete()
        actors = Actor.query.filter(Actor.name == 'Tom Hanks').all()
        for actor in actors:
            actor.delete()
        pass

    def test_get_actors(self):
        res = self.client().get(
            '/actors', headers=self.assistantHeader)
        data = json.loads(res.data)

        actors = [actor.format() for actor in Actor.query.all()]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actors'], actors)
        self.assertEqual(data['total_actors'], len(actors))

    def test_error_401_read_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'],
                         'Authorization header is expected.')

    def test_get_movies(self):
        res = self.client().get(
            '/movies', headers=self.assistantHeader)
        data = json.loads(res.data)

        movies = [movie.format() for movie in Movie.query.all()]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], movies)
        self.assertEqual(data['total_movies'], len(movies))

    def test_error_401_read_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'],
                         'Authorization header is expected.')

    def test_create_actor(self):
        res = self.client().post('/actors',
                                 headers=self.directorHeader,
                                 json=self.new_actor
                                 )
        data = json.loads(res.data)

        actors = [actor.format() for actor in Actor.query.all()]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actors'], actors)
        self.assertEqual(data['total_actors'], len(actors))

    def test_error_401_create_actor(self):
        res = self.client().post('/actors',
                                 headers=self.assistantHeader,
                                 json=self.new_actor
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_access_request')
        self.assertEqual(data['description'],
                         'You dont have permissions to access this resource')

    def test_error_400_create_actor(self):
        res = self.client().post('/actors',
                                 headers=self.directorHeader,
                                 json=self.invalid_actor
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'],
                         'Bad request')

    def test_create_movie(self):
        res = self.client().post('/movies',
                                 headers=self.producerHeader,
                                 json=self.new_movie
                                 )
        data = json.loads(res.data)

        movies = [movie.format() for movie in Movie.query.all()]
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], movies)
        self.assertEqual(data['total_movies'], len(movies))

    def test_error_401_create_movie(self):
        res = self.client().post('/movies',
                                 headers=self.directorHeader,
                                 json=self.new_movie
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_access_request')
        self.assertEqual(data['description'],
                         'You dont have permissions to access this resource')

    def test_error_400_create_movie(self):
        res = self.client().post('/movies',
                                 headers=self.producerHeader,
                                 json=self.invalid_movie
                                 )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'],
                         'Bad request')

    def test_update_actor(self):
        actor = Actor(
            self.update_actor_valid.get('name'),
            self.update_actor_valid.get('age'),
            self.update_actor_valid.get('gender')
        )
        actor.insert()
        actor_id = actor.id
        res = self.client().patch('/actors/' + str(actor_id),
                                  headers=self.directorHeader,
                                  json=self.update_actor_valid
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actors'][0].get('name'),
                         self.update_actor_valid.get('name'))

    def test_error_401_update_actor(self):
        res = self.client().patch('/actors/1',
                                  headers=self.assistantHeader,
                                  json=self.update_actor_valid
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_access_request')
        self.assertEqual(data['description'],
                         'You dont have permissions to access this resource')

    def test_error_400_update_actor(self):
        res = self.client().patch('/actors/1',
                                  headers=self.directorHeader,
                                  json=self.invalid_actor
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'],
                         'Bad request')

    def test_update_movie(self):
        movie = Movie(self.update_movie_valid.get('title'),
                      self.update_movie_valid.get('release_date'))
        movie.insert()
        movie_id = movie.id
        res = self.client().patch('/movies/' + str(movie_id),
                                  headers=self.producerHeader,
                                  json=self.update_movie_valid
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'][0].get('title'),
                         self.update_movie_valid.get('title'))

    def test_error_401_update_movie(self):
        res = self.client().patch('/movies/1',
                                  headers=self.assistantHeader,
                                  json=self.update_movie_valid
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_access_request')
        self.assertEqual(data['description'],
                         'You dont have permissions to access this resource')

    def test_error_400_update_movie(self):
        res = self.client().patch('/movies/1',
                                  headers=self.producerHeader,
                                  json=self.invalid_movie
                                  )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'],
                         'Bad request')

    def test_delete_movie(self):
        movie = Movie(self.update_movie_valid.get('title'),
                      self.update_movie_valid.get('release_date'))
        movie.insert()
        movie_id = movie.id
        res = self.client().delete('/movies/' + str(movie_id),
                                   headers=self.producerHeader
                                   )
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], movie_id)
        self.assertEqual(movie, None)

    def test_error_401_delete_movie(self):
        res = self.client().delete('/movies/1',
                                   headers=self.assistantHeader
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_access_request')
        self.assertEqual(data['description'],
                         'You dont have permissions to access this resource')

    def test_error_404_delete_movie(self):
        res = self.client().delete('/movies/1000',
                                   headers=self.producerHeader
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'],
                         'Resource not found')

    def test_delete_actor(self):
        actor = Actor(
            self.update_actor_valid.get('name'),
            self.update_actor_valid.get('age'),
            self.update_actor_valid.get('gender')
        )
        actor.insert()
        actor_id = actor.id
        res = self.client().delete('/actors/' + str(actor_id),
                                   headers=self.producerHeader
                                   )
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], actor_id)
        self.assertEqual(actor, None)

    def test_error_401_delete_actor(self):
        res = self.client().delete('/actors/1',
                                   headers=self.assistantHeader
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'invalid_access_request')
        self.assertEqual(data['description'],
                         'You dont have permissions to access this resource')

    def test_error_404_delete_actor(self):
        res = self.client().delete('/actors/1000',
                                   headers=self.producerHeader
                                   )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'],
                         'Resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
