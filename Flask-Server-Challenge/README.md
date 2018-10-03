## Flask Server Challenge

Ada wants to plan the next developers meetup. As tasks stack up, she thinks that a todo list app might help her manage the event better. 

She recalls she had frontend for a simple Android ToDo List App she developed in a previous dev meet. But she lacks the backend for it. Since she has a lot of work to do, she can't develop the server so soon.

## Task 
Her Ada by developing a simple Flask web server for her ToDo list app.


### Level 0 - Flask basics
Create a simple Flask server with two basic methods  

API End Point | Type | Required Body Params   | Required Return Value
--------------|------|--------                | ------------------------- 
/sample_get     | GET  | NA                     | String "Hello Flask" without quotes
/sample_post    | POST | name(string)           | String "Hello to Flask, <name>", where name is supplied as a POST parameter


### Level 1 - Database Intregration
Create a simple Flask server that with some basic methods - maintain a serial list of tasks(numbered 1,2,3...). You're free to keep the database local or hosted somewhere.

API End Point | Type | Body Params   | Return value(apart from `status`)    |Description
--------------|------|--------                | ------------------------- | -------------
/list_all     | GET  | NA                     | task[](list of strings)  | Get the list of tasks to be done
/append       | POST | task(string)           | NA | Append a task to the list
/insert       | POST | task(string), index(int)| NA | Insert a task between indices (index,index+1)
/delete       | DELETE | index(int)           | task(string) | Delete task at given index. Return the deleted task


### Resources
+ Intro to Flask - https://www.fullstackpython.com/flask.html
+ Handling REST Requests - https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
+ Flask Auth - https://realpython.com/token-based-authentication-with-flask/
+ Flask DB Introducion - http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
+ Flask Postgres - https://blog.theodo.fr/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/
+ Google Text to Speech API in Python - https://www.geeksforgeeks.org/convert-text-speech-python/
+ Flask Caching - https://realpython.com/python-memcache-efficient-caching/

### More Info
+ You need not host the server
+ The body content should be `json` encoded.
+ `status` param is mandatory for all end points. Its value is `200` for success, `404` for URL not found, etc. Refer [this doc](https://www.restapitutorial.com/httpstatuscodes.html) for a complete list.
