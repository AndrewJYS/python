from flask import Flask
from search_for_letters import search_for_letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    """Returns the set of 'letters' found in 'phrase'."""
    return str(search_for_letters('life, the universe, and everything', 'eiru,!'))

app.run()