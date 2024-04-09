import os
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer
from opencensus.ext.azure.trace_exporter import AzureExporter
from azure.storage.queue import QueueClient
from constant import env_credentials
from dotenv import load_dotenv

load_dotenv(env_credentials)
InstrumentationKey = os.environ["InstrumentationKey"]
storage_name = os.environ["storage_name"]
storage_access_key = os.environ["storage_access_key"]
queue_name = os.environ["queue_name"]

# # Initialize the QueueClient
queue_client = QueueClient.from_connection_string(conn_str=f"DefaultEndpointsProtocol=https;AccountName={storage_name};AccountKey={storage_access_key};EndpointSuffix=core.windows.net", queue_name=queue_name)

tracer = Tracer(
    exporter=AzureExporter(connection_string=f'InstrumentationKey={InstrumentationKey}'),
    sampler=ProbabilitySampler(1.0)
)

# Start tracing the dependency
with tracer.span(name="Add Message To Queue") as span:
    # Define the message content
    message_content = 'Hello from Azure Queue!'
    
    # Add message to the queue
    queue_client.send_message(message_content)
    span.add_attribute("custom_attribute1", "value1")
    span.add_attribute("custom_attribute2", "value2")
