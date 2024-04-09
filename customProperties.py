import os
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from constant import env_credentials
from dotenv import load_dotenv

load_dotenv(env_credentials)
InstrumentationKey = os.environ["InstrumentationKey"]

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={InstrumentationKey}'))

properties = {'custom_dimensions': {'name': 'xyz', 'count': 47}}
logger.warning('action', extra=properties)