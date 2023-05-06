# SubjectList
### GET
``curl -X GET http://127.0.0.1:8000/api/subjects/
``
### POST
``
curl -X POST http://127.0.0.1:8000/api/subjects/ 
  -H 'Content-Type: application/json' 
  -d '{"name": "Chemistry", "instructors": [1, 2, 3]}'
``
