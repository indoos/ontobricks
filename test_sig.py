from databricks.sdk.service import database
import inspect

print(inspect.signature(database.DatabaseAPI.generate_database_credential))
