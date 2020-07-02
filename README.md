# Casting Agency

## Introduction

This application models a company that is responsible for creating movies and managing and assigning actors to those movies and streamline the process.

## Specifications

### Models:

* Movies with attributes title and release date
* Actors with attributes name, age and gender

### Endpoints:
* GET /actors and /movies
* DELETE /actors/ and /movies/
* POST /actors and /movies and
* PATCH /actors/ and /movies/

### Roles:
* Casting Assistant: 
    - Can view actors and movies
* Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
* Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

### Tests:
* One test for success behavior of each endpoint
* One test for error behavior of each endpoint
* At least two tests of RBAC for each role

## Auth0 account
```python
AUTH0_DOMAIN = 'deedev.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'https://github.com/DeekshaPrabhakar/CastingAgency'
```

`The tokens may expire, so please use the login credentials below to generate a new JWT token`

### Assistant account
```
email: caassistant@gmail.com
password: apple123*
```
#### Token
```


```

### Director account
```
email: cadirector@gmail.com
password: apple123*
```
#### Token
```

```

### Producer account
```
email: caproducer@gmail.com
password: apple123*
```
#### Token
```

```

## Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Set up database using psql on command line:
  ```
  createdb CastingAgency
  ```

4. Run the development server:
  ```
  $ export FLASK_APP=app
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application requires authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable 
- 500: Server Error

### Endpoints 
#### GET /movies
- General:
    - Returns a list of movies
- Sample: `curl http://127.0.0.1:5000/movies`

``` 
{
    "movies": [
        {
            "id": 1,
            "release_date": "2006-05-19",
            "title": "The Da Vinci Code"
        }
    ],
    "success": true,
    "total_movies": 1
}
```

#### GET /actors
- General:
    - Returns a list of actors
- Sample: `curl http://127.0.0.1:5000/actors`

``` 
{
    "actors": [
        {
            "age": 51,
            "gender": "Male",
            "id": 1,
            "name": "Will Smithe"
        }
    ],
    "success": true,
    "total_actors": 1
}
```

#### POST /movies
- General:
    - Creates a new movie using the submitted title, release_date. 
- `curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d '{"title": "The Da Vinci Code", "release_date":"2006-05-19"}'`
```
{
    "created": 1,
    "movies": [
        {
            "id": 1,
            "title": "The Da Vinci Code",
            "release_date": "2006-05-19"
        }
    ],
    "success": true,
    "total_movies": 1
}
```

#### POST /actors
- General:
    - Creates a new actor using the submitted name, age, gender
- `curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d '{"name": "Will Smith", "age":"51", "gender":"Male"}'`
```
{
    "actors": [
        {
            "id": 1,
            "name": "Will Smith",
            "age": 51,
            "gender": "Male"
        }
    ],
    "created": 1,
    "success": true,
    "total_actors": 1
}
```


#### PATCH

```
{
    "actors": [
        {
            "age": 51,
            "gender": "Male",
            "id": 1,
            "name": "Will Smith"
        }
    ],
    "success": true
}
```

#### PATCH

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "2006-05-16",
            "title": "The Da Vinci Code"
        }
    ],
    "success": true
}
```

#### DELETE /actors/{actor_id}
- General:
    - Deletes the actor of the given ID if it exists. Returns the id of the deleted actor id, success value
- `curl -X DELETE http://127.0.0.1:5000/actors/1`
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/{movie_id}
- General:
    - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie id, success value
- `curl -X DELETE http://127.0.0.1:5000/movies/1`
```
{
    "deleted": 1,
    "success": true
}
```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
