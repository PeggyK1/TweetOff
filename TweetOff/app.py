"""Main app/routing file for TwitOff."""
from flask import Flask, render_template
from .models import DB, User
from .twitter import insert_example_users


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    # ... TODO make the app!
    @app.route('/')
    def root():
        return render_template('base.html', title='Home',
                               users=User.query.all())

    @app.route('/update')
    def update():
        # Reset the database
        insert_example_users()
        return render_template('base.html', title='Users updated!',
                               users=User.query.all())

    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    return app