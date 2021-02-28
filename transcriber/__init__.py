import os
import sys
import hashlib
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://flaskr.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        DEBUG=True,
        FLASK_ENV="development",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['dafile']
            saved = "/".join(['uploads', f.filename])
            f.save(saved)
            # create entry in db about the new file bind it to new user
            # daemon process file and create flac 1 channel
            # upload_to_bucket(bucket_name='dev-test-rodderscode-co-uk', filename=saved)
            # process in google and get token
            # save token to db against file
            # access page 
        return redirect('/')

    def upload_to_bucket(bucket_name, filename):
        from libs.bucket import Bucket
        from libs.gfiles import GFiles
        Bucket().create_bucket(bucket_name)
        GFiles(bucket_name).upload(filename)

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     db_session.remove()
        
    
    return app


if __name__ == "__main__":
    app = create_app()
    # from app.db import * 
    # db.init_db()
    app.run(debug=True)