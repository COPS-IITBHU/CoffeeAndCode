## Flask Server Challenge

Ada wants to plan the next developers meetup. As tasks stack up, she thinks that a todo list app might help her manage the event better. 

She recalls she had frontend for a simple Android ToDo List App she developed in a previous dev meet. But she lacks the backend for it. Since she has a lot of work to do, she can't develop the server so soon.

## Task 
Her Ada by developing a simple Flask web server for her ToDo list app.


### Level 0 - Easy - Flask basics
Create a simple Flask server with two basic methods  

API End Point | Type | Required Body Params   | Required Return Value
--------------|------|--------                | ------------------------- 
/sample_get     | GET  | NA                     | String "Hello Flask" without quotes
/sample_post    | POST | name(string)           | String "Hello to Flask, <name>", where name is supplied as a POST parameter 
  
  
  
### Level 1 - Easy - Database Intregration
Create a simple Flask server that with some basic methods - maintain a serial list of tasks(numbered 1,2,3...). You're free to keep the database local or hosted somewhere.

API End Point | Type | Body Params   | Return value(apart from `status`)    |Description
--------------|------|--------                | ------------------------- | -------------
/list_all     | GET  | NA                     | task{}(list of strings)  | Get the list of tasks to be done
/append       | POST | task(string)           | NA | Append a task to the list
/insert       | POST | task(string), index(int)| NA | Insert a task between indices (index,index+1)
/delete       | DELETE | index(int)           | task(string) | Delete task at given index. Return the deleted task


### Level 2 - Medium - Speech to Text
Ada thinks dictation will be faster typing. So she wants to store tasks via voice.  

There are many engines available for speech to text conversion(follow [this article](https://www.quora.com/What-are-the-top-ten-speech-recognition-APIs) for a complete list). You need to add a new features to create a task using speech.  

API End Point | Type | Body Params   | Return value(apart from `status`)    |Description
--------------|------|--------                | ------------------------- | -------------
/append_speech       | POST | audio_task(base64 encoded string)           | NA | Append a task to the list
/insert_speech       | POST | audio_task(base64 encoded string), index(int)| NA | Insert a task between indices (index,index+1)  

**Note**: Refer resources for details about base64. Its important for sending media data over REST APIs



### Level 3 - Hard - Undo/Redo Features
Ada types really bad(thats why she prefer to use voice). And also she prefers undoing typing a task rather than correcting it. 

Manage the history of tasks entered and deleted. In this sense, `undo` means going one step back in history(which might mean deleting a task or restoring a deleted task) and `redo` means one step in future. This might seem easy at first glance, but *you'll need to develop a mini git of your own!*. There are many ways to version data. Refer [this](https://homes.cs.washington.edu/~mernst/advice/version-control.html) and [this article](https://www.atlassian.com/git/tutorials/what-is-version-control) for more.

API End Point | Type | Body Params   | Return value(apart from `status`)    |Description
--------------|------|--------                | ------------------------- | -------------
/undo       | GET | NA           | task{}(list of strings) | List of tasks viewed as one step back in history
/redo       | GET | NA  | task{}(list of strings) | List of tasks viewed as one step ahead in future

**Note**: You can't undo with no tasks. Similarly, you can't redo when already at the lastest list of tasks.


### Evaluation Criteria
There's no marking criteria(Remember you're just hepling Ada ;D ). The levels arranged in increasing order of difficulty. For testing purposes, keep your file structured in such a way that the main serving file is named `app.py` or the evaluators should be able to run server using the following commands:
```bash
export FLASK_APP=app.py
flask run
```

### Resources
+ Intro to Flask - https://www.fullstackpython.com/flask.html
+ Handling REST Requests - https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
+ Flask Auth - https://realpython.com/token-based-authentication-with-flask/
+ Flask DB Introducion - http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
+ Flask Postgres - https://blog.theodo.fr/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/
+ Google Text to Speech API in Python - https://www.geeksforgeeks.org/convert-text-speech-python/
+ Flask Caching - https://realpython.com/python-memcache-efficient-caching/
+ Uploading Files via HTTP requests - https://medium.com/@petehouston/upload-files-with-curl-93064dcccc76
+ Base64 encoding - https://cloud.google.com/speech-to-text/docs/base64-encoding

### More Info
+ You need not host the server
+ The body content should be `json` encoded.
+ `status` param is mandatory for all end points. Its value is `200` for success, `404` for URL not found, etc. Refer [this doc](https://www.restapitutorial.com/httpstatuscodes.html) for a complete list.
