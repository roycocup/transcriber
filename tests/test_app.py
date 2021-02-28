import os
import tempfile

import pytest

from app.flask_bootstrap import *

@pytest.fixture
def client():
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with flaskr.app.app_context():
            # flaskr.init_db()
            print(app.config['DATABASE'])
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])