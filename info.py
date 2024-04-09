import os
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
from constant import env_credentials
from dotenv import load_dotenv

load_dotenv(env_credentials)
InstrumentationKey = os.environ["InstrumentationKey"]

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={InstrumentationKey}'))
logger.setLevel(logging.INFO)

logger.info('Script executed')