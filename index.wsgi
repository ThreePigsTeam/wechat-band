import sys
import os
import sae
from manage import manager

application = sae.create_wsgi_app(manager)