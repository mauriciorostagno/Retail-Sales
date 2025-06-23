import duckdb
import os
import pandas as pd

# Relative paths
current_dir = os.path.dirname(os.path.abspath(__file__))
input_csv_path = os.path.join(current_dir, "..", "data", "raw", "Online Retail Data Set.csv")
output_db_path = os.path.join(current_dir, "..", "warehouse", "online_retail.duckdb")

# Read CSV
df = pd.read_csv(input_csv_path, encoding="ISO-8859-1")  # utf-8 or iso?

# For making sure output file exists
os.makedirs(os.path.dirname(output_db_path), exist_ok=True)

# Connection to DuckDB (only if it doesn't exist yet)
con = duckdb.connect(database=output_db_path)

# Save table in DuckDB (replace the table if it exists)
con.execute("DROP TABLE IF EXISTS online_retail")
con.execute("""CREATE TABLE online_retail AS
             SELECT
                InvoiceNo AS id_invoice,
                StockCode AS code_stock,
                Description AS name,
                Quantity AS quantity,
                InvoiceDate AS invoice_date,
                UnitPrice AS price_per_unit,
                CustomerID AS id_customer,
                CASE
                  WHEN Country = 'United Kingdom' THEN 'UK'
                  ELSE Country
                END AS country
              FROM df
            """)

# End
con.close()

print("✅ Dataset loaded succesfully to DuckDB in:", output_db_path)
