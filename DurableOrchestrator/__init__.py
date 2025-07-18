import azure.durable_functions as df

def main(context: df.DurableOrchestrationContext):
    input_data = context.get_input()
    metadata = yield context.call_activity("ExtractMetadata", input_data)
    yield context.call_activity("StoreMetadata", metadata)
    return metadata