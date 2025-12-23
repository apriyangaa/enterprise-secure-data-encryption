"""
AES column-level encryption pattern using Databricks Secret Scopes
Applied to sensitive fields in regulated datasets
"""

from pyspark.sql.functions import expr

# Retrieve AES key from secret scope (placeholder)
AES_KEY = dbutils.secrets.get(
    scope="SECURITY_SCOPE",
    key="AES_KEY"
)

# Example dataframe assumed to be present
secure_df = df.withColumn(
    "salary_encrypted",
    expr("encrypt(salary, AES_KEY)")
)

secure_df.display()
