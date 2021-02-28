from app.flask_bootstrap import *

if __name__ == "__main__":
    app = create_app()
    # from app.db import * 
    # db.init_db()
    app.run(debug=True)