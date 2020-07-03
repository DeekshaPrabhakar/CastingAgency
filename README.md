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

`The tokens will expire on July 12th`

### Assistant account
```
email: caassistant@gmail.com
password: apple123*
```
#### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiTThPNlNLd0ZGdVhEV3RIYU9ncDBHVkZqclhBRjMyelhAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZ2l0aHViLmNvbS9EZWVrc2hhUHJhYmhha2FyL0Nhc3RpbmdBZ2VuY3kiLCJpYXQiOjE1OTM3MzI4OTEsImV4cCI6MTU5NDU5Njg5MSwiYXpwIjoiTThPNlNLd0ZGdVhEV3RIYU9ncDBHVkZqclhBRjMyelgiLCJzY29wZSI6InJlYWQ6YWN0b3JzIHJlYWQ6bW92aWVzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.4Sq0J_7--iMSeBPpyYC47-Pd6x-yKoV5hXM3MPMzYdkJuL40ejekG4--X4E_pIe_bO9MWGdtuxm6h8IhvwBRtgXH8RJpSUv9iE1CPnxwedYBOOvDZkHLdrDB2nS0zNyzf5JKsFkAQoxN4L04ngRHyNkZVzNyxenopXw5kg8g2edQDqXDR5CDzKahT3-DYOPgcrauxuclckkha_YH3aqJG2SMubl0UsSF0NM7Kl8Gd6D1h9amHtkggpP-I4GvKRiiTCfcn8PilC14fM6OZD3ps2xxsLmpxoyUrgOjsLG0cSExu2fNjkiZ_xhH5mlWW6KYvJG0htLkrV11kdjyTbAWEA

```

### Director account
```
email: cadirector@gmail.com
password: apple123*
```
#### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiTThPNlNLd0ZGdVhEV3RIYU9ncDBHVkZqclhBRjMyelhAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZ2l0aHViLmNvbS9EZWVrc2hhUHJhYmhha2FyL0Nhc3RpbmdBZ2VuY3kiLCJpYXQiOjE1OTM3MzMwMDQsImV4cCI6MTU5NDU5NzAwNCwiYXpwIjoiTThPNlNLd0ZGdVhEV3RIYU9ncDBHVkZqclhBRjMyelgiLCJzY29wZSI6InJlYWQ6YWN0b3JzIGNyZWF0ZTphY3RvciBkZWxldGU6YWN0b3IgdXBkYXRlOmFjdG9yIHVwZGF0ZTptb3ZpZSByZWFkOm1vdmllcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbInJlYWQ6YWN0b3JzIiwiY3JlYXRlOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIiwicmVhZDptb3ZpZXMiXX0.gy1FkDXBJIHXMjgshQvj6NM7Ym-bdrThrObHi3F0aigu5xNBt7v3tRq7a9jfbeIcA6JTyh1WnXwuQLEKJuvvDCtVhgOsWJ6cw-rJGL_Mod-ZV6F4AkSvjJKL6SnY-CbZo6T2Mz_QTeblaXDB5u13-vcD5q9MyGqZ5LPnyFIvOyfiUx38nrGrCpvvntZe5NSSYa5xeB-Os_ybsW8rh4fzd1EkG7g8ZGFUaGqP-KsSD2vF4-lmuwbjwafSkdrXNaBZ3muZB_YibId0yuAtQjqOaj6S9_HGIzlHDs0at1Uvp8zuqz9Km8ilJH0Nw2tB_6Vz1kziY-CzZmiUe6QBY8Fa9g
```

### Producer account
```
email: caproducer@gmail.com
password: apple123*
```
#### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiTThPNlNLd0ZGdVhEV3RIYU9ncDBHVkZqclhBRjMyelhAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZ2l0aHViLmNvbS9EZWVrc2hhUHJhYmhha2FyL0Nhc3RpbmdBZ2VuY3kiLCJpYXQiOjE1OTM3MzMxNDMsImV4cCI6MTU5NDU5NzE0MywiYXpwIjoiTThPNlNLd0ZGdVhEV3RIYU9ncDBHVkZqclhBRjMyelgiLCJzY29wZSI6InJlYWQ6YWN0b3JzIGNyZWF0ZTphY3RvciBkZWxldGU6YWN0b3IgdXBkYXRlOmFjdG9yIGNyZWF0ZTptb3ZpZSBkZWxldGU6bW92aWUgdXBkYXRlOm1vdmllIHJlYWQ6bW92aWVzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsicmVhZDphY3RvcnMiLCJjcmVhdGU6YWN0b3IiLCJkZWxldGU6YWN0b3IiLCJ1cGRhdGU6YWN0b3IiLCJjcmVhdGU6bW92aWUiLCJkZWxldGU6bW92aWUiLCJ1cGRhdGU6bW92aWUiLCJyZWFkOm1vdmllcyJdfQ.rSYO06LliGk42bR00TsQQSkCKH9--Qdm_pfTYJv-F2kSiTnVvWbc8MJWysJKH4_iJPSY61xhdVcx3BOM_tI2ASlGxRbZWMwps2Iqe74ORZV4xCVNwijaYO1lzDsBRdDBpQzwmjrdE6tfhLTM4o2ROsjHBcMbrAKe7r_8LAXqq7uTfCwLownHNd8H4Q2PLQZw0OO4YOSrEQlis9NsYymO3sYtWtDBF22YRuITA60svRnQTxlh6ygWfxk7Aik2pQZnfh15wsqKFLbB7Nd9gSt5KmtxGB29Iv5rQn7_qAdzivYLoJR6aKgdHhemKXN50c6pJAMWVwO_E4wwU-tFMiuR7g
```

### Permissions
* `create:actor`: Create actor
* `read:actors`: View actors
* `update:actor`: Update actor
* `delete:actor`: Delete actor
* `create:movie`: Create movie
* `read:movies`: View movies
* `update:movie`: Update movie
* `delete:movie`: Delete movie

### Roles
* Casting Assistant: Can view actors and movies
* Casting Director: Can	create, read, update, delete actors, read and update movies
* Executive Producer: Can create, read, update, delete actors and movies

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
  dropdb casting
  createdb casting
  ```

4. Run the development server:
  ```
  $ export FLASK_APP=app
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)

## Live Server URL
> `https://acastingagency.herokuapp.com/`

## API Reference

> You can test the API endpoints using the live postman collection available in the project

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
```
{
    "actors": [
        {
            "id": 1,
            "name": "Will Smithe",
            "age": 51,
            "gender": "Male"
        }
    ],
    "created": 1,
    "success": true,
    "total_actors": 1
}
```


#### PATCH/actors/{actor_id}
- General:
    - Updates an existing actor using the submitted name, age, gender

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

#### PATCH/movies/{movie_id}
- General:
    - Updates and existing movie using the submitted title, release_date. 

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
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/{movie_id}
- General:
    - Deletes the movie of the given ID if it exists. Returns the id of the deleted movie id, success value
```
{
    "deleted": 1,
    "success": true
}
```



## Testing
To run the tests, run
```
dropdb casting_agency_test
createdb casting_agency_test
python test_app.py
```

