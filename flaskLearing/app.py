from flask import *
from datetime import datetime
from functools import wraps


app = Flask(__name__)
app.secret_key = 'password123'  # Secret key for session management
# Global context processor
@app.context_processor
def inject_year():
    return {'year': datetime.now().year}
# 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'loged_in' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def is_user_logged_in():
    return 'loged_in' in session and session['loged_in']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
     return render_template('about.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Check if user is already logged in
    is_login = is_user_logged_in()
    if is_login:
        flash('You are already logged in.')
        return redirect(url_for('login_success'))
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['loged_in'] = True
            return redirect(url_for('login_success'))
        else:
            flash('Invalid username or password.')
            return render_template('login_failure.html')
    
    return render_template('login.html')
@app.route('/logout/')
def logout():
    session.pop('loged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/login_success/')
@login_required
def login_success():
    return render_template('login_success.html')


if __name__ == '__main__':
    app.run(debug=True)

