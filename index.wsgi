import sys
import os
import sae
from server import app

app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'wechat-python-sdk-master'))

application = sae.create_wsgi_app(app)