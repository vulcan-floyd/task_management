import pytest
import os

from main import create_app, init_api
from extensions import db

from db_setup.mysql_setup import mysql_setup


@pytest.fixture(scope='module')
def test_client():
    # os.environ['CONFIG_TYPE'] = 'TestingConfig'
    # application = create_app('testing')
    application = create_app()
    application = init_api(application)
    with application.app_context():
        db.create_all()
        mysql_setup()
        
    with application.test_client() as testing_client:
        # Establish an application context
        with application.app_context():
            yield testing_client 
    
