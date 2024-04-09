import os
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
from constant import env_credentials
from dotenv import load_dotenv

load_dotenv(env_credentials)
InstrumentationKey = os.environ["InstrumentationKey"]
logger = logging.getLogger(__name__)
handler = AzureLogHandler(connection_string=f'InstrumentationKey={InstrumentationKey}')
logger.addHandler(handler)

# Start tracing the dependency
logger.warning('This is warning')