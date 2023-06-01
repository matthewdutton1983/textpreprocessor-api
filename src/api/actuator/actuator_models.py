# Import third-party libraries
from flask_restx import Namespace

actuator_ns = Namespace("actuator", description="This service provides information about the overall health of the system.")
