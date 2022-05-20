# Session  

## flask-session  

运行下述代码，我们发现，不同浏览器（不同客户）的用户信息是独立的，用户A不能看到用户B的user信息。原因是，通过在各个浏览器中自动设置一个唯一的cookie，web应用使用Session字典，可以为各个浏览器分别维护一个针对浏览器的user值  

```python
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess' # secret_key必须加上

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
    app.run(debug=True)
```

## 参考  

Head First Python Chapter 10  
