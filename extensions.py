# from flask_statsd import Statsd
from flasgger import Swagger
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
# statsd = Statsd()
SWAGGER_TEMPLATE = {
   "securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name": "x-access-token", "in": "header"}}}
swagger = Swagger(template=SWAGGER_TEMPLATE)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
