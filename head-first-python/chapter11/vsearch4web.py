from flask import Flask, render_template, request, session, copy_current_request_context
import sys
from threading import Thread
from time import sleep

from search_for_letters import search_for_letters
from DBcm import UseDatabase, ConnectionError, SQLError
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecretKey'

app.config['dbconfig'] = { 'host':'localhost',
                           'user': 'root',
                           'password': 'root',
                           'db': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Log details of the web request and the results."""
        sleep(15)
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = 'insert into log ' \
                   '(phrase, letters, ip, browser_string, results)' \
                   'values ' \
                   '(%s, %s, %s, %s, %s)'
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search_for_letters(phrase, letters))

    try:
        # log_request(request, results)
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('*****Logging failed with this error:', str(err))

    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/', methods=['GET', 'POST'])
@app.route('/entry', methods=['GET', 'POST'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = 'select phrase, letters, ip, browser_string, results ' \
                   'from log'
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('phrase', 'letters', 'ip', 'browser_string', 'results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents, )
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', sys.exc_info())
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)