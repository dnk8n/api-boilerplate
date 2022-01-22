import logging
import os

log_level = os.getenv("LOGLEVEL", "WARNING").upper()
log_format = "[%(asctime)s %(filename)10s->%(funcName)s():%(lineno)s] %(levelname)10s: %(message)s"
logging.basicConfig(level=log_level, format=log_format)
logger = logging.getLogger(__name__)
