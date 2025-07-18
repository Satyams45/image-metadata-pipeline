# 🧠 Image Metadata Processing Pipeline

## 📚 CST8917 Assignment 1 — Durable Workflow for Image Metadata Processing

This project demonstrates a complete serverless pipeline using **Azure Durable Functions in Python**. It processes user-uploaded images in real-time by extracting metadata and storing it in **Azure SQL Database**.

---

## 📦 Features

✅ Automatically triggers on image upload to Azure Blob Storage (`images-input`)  
✅ Uses Durable Functions Orchestrator pattern  
✅ Extracts metadata using Pillow and Requests  
✅ Stores metadata in Azure SQL using output bindings or pyodbc  
✅ Written in Python and deployable to Azure Function App  

---

## 🗂️ Folder Structure

```
image-metadata-pipeline/
├── BlobTrigger/             # Blob Trigger Function
│   ├── __init__.py
│   └── function.json
├── Orchestrator/            # Durable Orchestrator Function
│   ├── __init__.py
│   └── function.json
├── ExtractMetadata/         # Activity: Extract Metadata
│   ├── __init__.py
│   └── function.json
├── StoreMetadata/           # Activity: Store to SQL
│   ├── __init__.py
│   └── function.json
├── requirements.txt         # Python dependencies
├── local.settings.json      # Azure local dev config
├── host.json                # Host settings for Azure Functions
└── README.md                # Project documentation
```

---

## 📷 Workflow Diagram

```mermaid
graph TD;
    A[Image Uploaded to Blob Storage] --> B[BlobTrigger Function]
    B --> C[Orchestrator Function]
    C --> D[ExtractMetadata Activity]
    C --> E[StoreMetadata Activity]
    E --> F[Azure SQL Database]
```

---

## 🧪 Local Development Setup

### ✅ 1. Clone the Repo
```bash
git clone https://github.com/Satyams45/image-metadata-pipeline.git
cd image-metadata-pipeline
```

### ✅ 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### ✅ 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### ✅ 4. Configure `local.settings.json`

Create a `local.settings.json` in the root:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "<your-storage-connection-string>",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "SQL_CONNECTION_STRING": "Driver={ODBC Driver 18 for SQL Server};Server=tcp:<your-sql-server>.database.windows.net;Database=ImageMetadataDB;Uid=<username>;Pwd=<password>;Encrypt=yes;"
  }
}
```

---

## 🛠️ Azure SQL Setup

### ✅ Create the Table
```sql
CREATE TABLE ImageMetadata (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(255),
    size_kb FLOAT,
    width INT,
    height INT,
    format NVARCHAR(50)
);
```

---

## ☁️ Deploy to Azure

### ✅ 1. Create Azure Resources
```bash
az group create --name metadata-rg --location eastus

az storage account create --name imagemetadatastg --resource-group metadata-rg --location eastus --sku Standard_LRS

az functionapp create
--name imageMetadataFunctionApp
--resource-group metadata-rg
--storage-account imagemetadatastg
--consumption-plan-location eastus
--runtime python
--functions-version 4
```

### ✅ 2. Deploy the Function App
```bash
func azure functionapp publish imageMetadataFunctionApp
```

---

## 🧪 Test the Pipeline

1. Upload a `.jpg`, `.png`, or `.gif` to the `images-input` container.
2. Use **Azure Storage Explorer** or portal.
3. Check Azure Logs / Console Output.
4. Validate metadata is stored in SQL DB.

---

## 👨‍💻 Author

Satyam Panseriya — CST8917, Algonquin College
