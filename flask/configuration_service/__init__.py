__author__ = 'rthompson'

def configure(app):
    app.secret_key = 'super secret string'  # Change this!
    # Configure app settings
    app.config['DEBUG'] = False

    # Create dummy secret key so we can use sessions
    app.config['SECRET_KEY'] = '123456790'

    # Create in-memory database
    app.config['DATABASE_FILE'] = 'cit.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/' + app.config['DATABASE_FILE']
    app.config['SQLALCHEMY_ECHO'] = True