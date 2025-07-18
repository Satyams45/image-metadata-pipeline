import azure.durable_functions as df

# Register orchestrator
orchestrator = df.Orchestrator.create(__import__("Orchestrator.__init__").main)

# Register activities
extract_metadata = df.ActivityTrigger.create(__import__("ExtractMetadata.__init__").main)
store_metadata = df.ActivityTrigger.create(__import__("StoreMetadata.__init__").main)

app = df.DFApp()
app.register_orchestrator(orchestrator)
app.register_activity(extract_metadata)
app.register_activity(store_metadata)
