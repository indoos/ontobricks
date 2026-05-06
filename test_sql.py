import os
from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="adb-6939737255485170")
warehouse_id = "b104fee28afe6079"
client_id = "20aacf53-946a-4762-a56d-aecb031c04df"

queries = [
    f"GRANT USE CATALOG ON CATALOG deprd_gpd TO `{client_id}`",
    f"GRANT USE SCHEMA ON SCHEMA deprd_gpd.onto_schema TO `{client_id}`",
    f"GRANT CREATE TABLE ON SCHEMA deprd_gpd.onto_schema TO `{client_id}`",
    f"GRANT MODIFY ON SCHEMA deprd_gpd.onto_schema TO `{client_id}`"
]

for query in queries:
    print(f"Executing: {query}")
    try:
        response = w.statement_execution.execute_statement(
            statement=query,
            warehouse_id=warehouse_id,
            wait_timeout="50s"
        )
        print("Success!")
    except Exception as e:
        print(f"Failed: {e}")
