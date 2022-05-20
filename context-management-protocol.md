# The context management protocol

It dictates that any class you create must define at least two magic methods: **\_\_enter\_\_** and **\_\_exit\_\_**. This is the protocol. When you adhere to the protocol, your class can hook into the with statement.  

When an object is used with a with statement, the interpreter invokes the object’s **\_\_enter\_\_** method before the **with** statement’s suite starts. **The protocol further states that dunder enter can (but doesn’t have to) return a value to the with statement.**

As soon as the with statement’s suite ends, the interpreter always invokes the object’s **\_\_exit\_\_** method. As the code in the with statement’s suite may fail (and raise an exception), **dunder exit** has to be ready to handle this if it happens.

## Examples  

We use the following programmes as an example.  

```python
## DBcm.py
import pymysql

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = pymysql.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
```

```python
## app.py
from flask import Flask, render_template, request, escape
from search_for_letters import search_for_letters
from DBcm import UseDatabase

def log_request(req: 'flask_request', res :str) -> None:
    dbconfig = { 'host':'localhost',
                 'user': 'root',
                 'password': 'root',
                 'db': 'vsearchlogDB', }

    with UseDatabase(dbconfig) as cursor:
        # it will return a cursor() to with statements by calling __enter__() of Class UseDatabase as defined in DBcm.py
        _SQL = 'insert into log ' \
               '(phrase, letters, ip, browser_string, results)' \
               'values ' \
               '(%s, %s, %s, %s, %s)'
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res))
        ## in the end, it will call __exit__() of Class UseDatabase
```

## references  

head First Python, Chapter 9  
