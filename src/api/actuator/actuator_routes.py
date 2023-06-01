# Import third-party libraries
from flask_restx import Resource

# Import project code
from .actuator_models import *
from log_config import Logger

logger = Logger().get_logger()

@actuator_ns.route("/health")
class ActuatorResource(Resource):
    def get(self):
        """
        Displays a message that confirms that the service is up and running.
        """
        return {"message": "Service is running"}, 200
