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
           --form 'refresh="<token>"'``


3. SubjectList
    1. **Description:** Lists and creates subject
    2. **URL:** `/api/subjects/`
    3. **Methods:** `GET` `POST`
    4. **Test cases:**
        1. Only stuff members can `POST` a subject: ``
           curl --location 'http://127.0.0.1:8000/api/subjects/'
           --header 'Authorization: <token>'
           --form 'instructors="1,2"'
           --form 'name="English"'
           ``
        2. All users can view subjects: `curl -X GET http://127.0.0.1:8000/api/subjects/`


4. SubjectDetails
    1. **Description:** updates and delete a subject
    2. **URL:** `/api/subjects/suject_id/`
    3. **Methods:** `PUT` `PATCH` `DELETE`
    4. **Test cases:**
        1. Only stuff members can `PUT` a
           subject: `curl --location --request PUT 'http://127.0.0.1:8000/api/subjects/2/' \
           --header 'Content-Type: application/json'
           --header 'Authorization: Bearer <token>'
           --data '{
           "name": "Maths",
           "instructors": [
           1,
           2
           ]
           }'`
        2. Only stuff members can `PATCH` a
           subject: `curl --location --request PATCH 'http://127.0.0.1:8000/api/subjects/2/' \
           --header 'Authorization: Bearer <token>' \
           --form 'name="Mathslit"'`
        3. Only stuff members can `DELETE` a
           subject: `curl --location --request DELETE 'http://127.0.0.1:8000/api/subjects/1/' \
           --header 'Authorization: Bearer <token>' \
           --form 'name="English"'`
        4. All users can view subject details: `curl -X GET http://127.0.0.1:8000/api/subjects/1/`


5. ProjectList
    1. **Description:** allows projects to be viewed or created.
    2. **URL:** `/api/projetcs/`
    3. **Methods:** `GET` `POST`
    4. **Test cases:**
        1. Users should only see projects they belong to: ``curl --location 'http://127.0.0.1:8000/api/projects/' \
           --header 'Authorization: Bearer <token>'``
        2. Users should see details of the project they belong
           to: `curl --location --request GET 'http://127.0.0.1:8000/api/projects/1/' \
           --header 'Authorization: Bearer <token>' \
           --form 'members="2"'`
        3. Only the creator of the project and the project subject instructor should be able to update and delete a
           project:
            4. Remove member from project: `curl --location --request PATCH 'http://127.0.0.1:8000/api/projects/1/' \
               --header 'Authorization: Bearer <token>' \
               --form 'remove_members="2"'`
            5. Add memeber to project: `curl --location --request PATCH 'http://127.0.0.1:8000/api/projects/1/' \
               --header 'Authorization: Bearer <token>' \
               --form 'members="2"'`


6. ProjectDetails


7. TaskList
    1. **Description:** allows project tasks to be viewed or created.
    2. **URL:** `/api/tasks/`
    3. **Methods:** `GET` `POST`
    4. **Test Cases**
        1. Only project members can view project
           tasks: `curl --location --request GET 'http://127.0.0.1:8000/api/tasks/' \
           --header 'Authorization: Bearer <token>' \`
        2. Only project members can create project tasks: `curl --location 'http://127.0.0.1:8000/api/tasks/' \
           --header 'Authorization: Bearer <token>' \
           --form 'title="Research about Algebra"' \
           --form 'description="Who invented algebra"' \
           --form 'project="1"' \
           --form 'due_date="2023-08-08"'`


8. TaskDetails
    1. **Description:** allows a task to be viewed, updated, or deleted.
    2. **URL:** `/api/tasks/`
    3. **Methods:** `PUT` `PATCH` `DELETE`
    4. **Test Cases**
        1. Only project members can `PUT` a project task:
        2. Only project members can `PATCH` a project task:
            1. Update task status: `curl --location --request PATCH 'http://127.0.0.1:8000/api/tasks/1/' \
               --header 'Authorization: Bearer <token>' \
               --form 'status="in_progress"'`
            2. Change assigned_to: `curl --location --request PATCH 'http://127.0.0.1:8000/api/tasks/1/' \
               --Update 'Authorization: Bearer <token>' \
               --form 'assigned_to="2"'`
        3. Only project members can `DELETE` a project
           task: `curl --location --request DELETE 'http://127.0.0.1:8000/api/tasks/2/' \
           --header 'Authorization: Bearer <token>' \
           --form 'project="1"'`