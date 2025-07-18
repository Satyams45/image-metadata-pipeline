import pyodbc
import os

def main(metadata: dict):
    conn_str = os.getenv("SQL_CONNECTION_STRING")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ImageMetadata (name, size_kb, width, height, format)
        VALUES (?, ?, ?, ?, ?)
    """, metadata["name"], metadata["size_kb"], metadata["width"], metadata["height"], metadata["format"])

    conn.commit()
    conn.close()