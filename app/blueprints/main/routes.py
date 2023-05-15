from flask import render_template, g

from . import bp
from app import app
from app.forms import UserSearchForm

@app.before_request
def before_request():
    g.user_search_form = UserSearchForm()

@bp.route('/')
def home():
    matrix = {
        'Movies': ('The Little Mermaid','Aladdin','Beauty and the Beast'),
        'students': ['Princess Ariel', 'Princess Jasmine','Princess Belle']
    }
    return render_template('index.jinja', title='Home', movies=matrix['Movies'],students=matrix['students'])
    
@bp.route('/about')
def about():
    return render_template('/about.jinja', user_search_form=g.user_search_form)

