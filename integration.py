import os
import requests
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace import config_integration
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer
from constant import env_credentials
from dotenv import load_dotenv

load_dotenv(env_credentials)
InstrumentationKey = os.environ["InstrumentationKey"]

config_integration.trace_integrations(['requests'])
tracer = Tracer(
    exporter=AzureExporter(
        connection_string=f'InstrumentationKey={InstrumentationKey}',
    ),
    sampler=ProbabilitySampler(1.0),
)
with tracer.span(name='parent'):
    response = requests.get(url='https://www.wikipedia.org/wiki/Rabbit')