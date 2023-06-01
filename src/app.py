# Import third-party libraries
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# Import project code
from api.api_instance import api
from api.actuator import actuator_routes
from api.encoder import encoder_routes
from api.flattener import flattener_routes
from api.normalizer import normalizer_routes
from api.processor import processor_routes
from api.segmenter import segmenter_routes
from api.transformer import transformer_routes
from log_config import Logger

logger = Logger().get_logger()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

namespaces = [
    actuator_routes.actuator_ns,
    encoder_routes.encoder_ns,
    flattener_routes.flattener_ns,
    normalizer_routes.normalizer_ns,
    processor_routes.processor_ns,
    segmenter_routes.segmenter_ns,
    transformer_routes.transformer_ns,
]

for namespace in namespaces:
    api.add_namespace(namespace)

if __name__ == '__main__':
    app.run(debug=True)
