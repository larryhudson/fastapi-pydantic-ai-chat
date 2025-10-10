# export_openapi.py
import json
from main import app

if __name__ == "__main__":
    schema = app.openapi()
    with open("openapi.json", "w") as f:
        json.dump(schema, f, indent=2)
    print("✅ Generated openapi.json")
