from flask import Flask

app = Flask(__name__)


@app.route('/')
def contents():
    return '/hello'


@app.route('/hello')
def hello_world():
    return 'Hello World!'

#
# @app.route('/books') def get_books():
# # Code to fetch all books from the database and return their details.
# @app.route('/books/<id>') def get_book(id):
# # Code to fetch the book entry with matching id from the database and
# return its details.
# @app.route('/books', methods=['POST']) def add_book():
# # Code to create a new book entry in the database.

#HTML templating -> using jinja2 - Flask uses the Jinja2 template engine
# @app.route('/books') def get_books():
#     books = get_all_books_from_db() # Some function that returns the list of book entries from the database.
# return render_template('book_list.html', books=books)


#Accessing request data

# from flask import request
# @app.route('/login', methods=['POST']) def login():
#     username = request.form['username'] password = request.form['password'] if valid_login(username, password):
#     return log_the_user_in(username) else:
# error = 'Invalid username/password'
# return render_template('login_error.html', error=error)