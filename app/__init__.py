from flask import Flask
import logging

logger = logging.getLogger("SERVICE")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s|%(name)-12s|%(levelname)-8s|%(message)s',
    datefmt='%m-%d %H:%M',
    filename='/temp/myapp.log',
    filemode='w'
)

flask_app = Flask("__PYTHON_REST_API_TEMPLATE__")


from .views import *
