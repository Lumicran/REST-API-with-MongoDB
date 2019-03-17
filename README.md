RESTful Flask API with MongoDB
__________________________________
This repo is an example of CREATE-READ-UPDATE-DELETE (CRUD) API in Python, based on Flask, and uses MongoDB as a database.

Tech/Framework Used
__________________________________
* Python
* Flask
* MongoDB

Getting Started/Installation
__________________________________
These instructions will get a copy of the project up and running on your local machine.

* Clone project onto local machine.
* Activate your environment.
  - pip install virtualenv
  - virtualenv env
  - source env/bin/activate
* Install requirements for project.
  - pip install -r requirements.txt
* Start mongoDB.
  mongod
* In a second tab, start flask instance.
  python3 server.py
* In a third tab, you can use and test the API by trying out the following commands:
  * To post (Create a new entry)
    - curl -v -XPOST -H "Content-Type: application/json" http://localhost:5000/info -d '{"name":"<string name>"}'
  * To get (Read an existing entry)
    - curl -v -XGET http://localhost:5000/info/<id # of entry>
  * To put (Update an existing entry)
    - curl -v -XPUT -H "Content-Type: application/json" http://localhost:5000/info/<id of entry> -d '{"name":"<update value"}'
  * To delete (Delete an existing entry)
    - curl -v -XDELETE http://localhost:5000/info/<id # of entry>
* Make sure to end the environment!
  - deactivate

Extra Notes
__________________________________
* If there are issues with bson (i.e. "cannot import name 'abc' from 'bson.py3compat'"), follow these directions to resolve:
  - Uninstall pymongo and reinstall with command:
    - python3 -m pip install pymongo

Misc
__________________________________
Information on CRUD in Python:
https://realpython.com/flask-connexion-rest-api/
