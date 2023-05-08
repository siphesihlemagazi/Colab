# **Endpoints**
## **SubjectList**
**Description:** Lists and creates subject

**URL:** `/api/subjects/`

**Methods:** `GET` `POST`

**Test cases:**
- Only stuff members can `POST` a subject.
  - ``
  curl --location 'http://127.0.0.1:8000/api/subjects/'
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5c...'
--form 'instructors="1,2"'
--form 'name="English"'
  ``
- All users can view subjects.
  - `curl -X GET http://127.0.0.1:8000/api/subjects/`

## **SubjectDetailss**
**Description:** updates and delete a subject

**URL:** `/api/subjects/suject_id/`

**Methods:** `PUT` `DELETE`

**Test cases:**
- Only stuff members can `PUT` and `DELETE` a subject.
  - `curl --location --request PUT 'http://127.0.0.1:8000/api/subjects/2/' \
--header 'Content-Type: application/json'
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiI...'
--data '{
    "name": "Maths",
    "instructors": [
        1,
        2
    ]
}'`
  - `curl --location --request PATCH 'http://127.0.0.1:8000/api/subjects/2/'
--header 'Content-Type: application/json'
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsI..'
--data '{
    "name": "Maths",
    "instructors": [
        2
    ]
}'`
- All users can view subject detailss.
  - `curl -X GET http://127.0.0.1:8000/api/subjects/1/`