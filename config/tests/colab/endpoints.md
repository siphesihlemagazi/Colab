# **Endpoints**

1. TokenObtainPairView
   1. **Description:** Takes a set of user credentials and returns an access and refresh JSON web
       token pair to prove the authentication of those credentials.
   2. **URL:** `/api/token/`
   3. **Methods:** `POST`
   4. **Test cases:**
      1. Users can get access token: `curl --location 'http://127.0.0.1:8000/api/token/' \
  --form 'email="user@colab.com"' \
  --form 'password="password"'`


2. TokenRefreshView
    1. **Description:** Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
   2. **URL:** `/api/token/refresh/`
   3. **Methods:** `POST`
   4. **Test Cases**
      1. Users can refresh token: ``curl --location 'http://127.0.0.1:8000/api/token/refresh/' \
--form 'refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."'``


3. SubjectList
   1. **Description:** Lists and creates subject
   2. **URL:** `/api/subjects/`
   3. **Methods:** `GET` `POST`
   4. **Test cases:**
      1. Only stuff members can `POST` a subject: ``
  curl --location 'http://127.0.0.1:8000/api/subjects/'
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5c...'
--form 'instructors="1,2"'
--form 'name="English"'
  ``
      2. All users can view subjects: `curl -X GET http://127.0.0.1:8000/api/subjects/`


4. SubjectDetails
   1. **Description:** updates and delete a subject
   2. **URL:** `/api/subjects/suject_id/`
   3. **Methods:** `PUT` `PATCH` `DELETE`
   4. **Test cases:**
      1. Only stuff members can `PUT` a subject: `curl --location --request PUT 'http://127.0.0.1:8000/api/subjects/2/' \
--header 'Content-Type: application/json'
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiI...'
--data '{
    "name": "Maths",
    "instructors": [
        1,
        2
    ]
}'`
      2. Only stuff members can `PATCH` a subject: `curl --location --request PATCH 'http://127.0.0.1:8000/api/subjects/2/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIs...' \
--form 'name="Mathslit"'`
      3. Only stuff members can `DELETE` a subject: `curl --location --request DELETE 'http://127.0.0.1:8000/api/subjects/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
--form 'name="English"'`
      4. All users can view subject details: `curl -X GET http://127.0.0.1:8000/api/subjects/1/`