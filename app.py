from app.flask_bootstrap import *

from transcriber.db import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app = create_app()
    # from app.db import * 
    # db.init_db()
    app.run(debug=True)