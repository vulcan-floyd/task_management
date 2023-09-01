import pytest
import os

from main import create_app, init_api
from extensions import db

from db_setup.mysql_setup import mysql_setup


@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    application = create_app('testing')
    application = init_api(application)
    with application.app_context():
        db.create_all()
        mysql_setup()
        
    # Create a test client using the Flask application configured for testing
    with application.test_client() as testing_client:
        # Establish an application context
        with application.app_context():
            yield testing_client 
    
