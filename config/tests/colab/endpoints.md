# **Endpoints**
## **SubjectList**
**Description:** Lists and creates subject

**URL:** `/api/subjects/`

**Methods:** `GET` `POST`

**Test cases:**
- Only stuff members can `POST`, `PUT` and `DELETE` a subject.
  - ``
  curl -X POST http://127.0.0.1:8000/api/subjects/ 
    -H 'Content-Type: application/json' 
    -d '{"name": "Chemistry", "instructors": [1, 2, 3]}'
  ``
- All users can view a subject and its details.
  - `curl -X GET http://127.0.0.1:8000/api/subjects/`
  - `curl -X GET http://127.0.0.1:8000/api/subjects/1/`
