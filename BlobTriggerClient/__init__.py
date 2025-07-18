import logging
import azure.functions as func
import azure.durable_functions as df

def main(blob: func.InputStream, starter: str):
    client = df.DurableOrchestrationClient(starter)
    instance_id = client.start_new("Orchestrator", None, {
        "name": blob.name,
        "data": blob.read()
    })
    logging.info(f"Started orchestration: {instance_id}")
