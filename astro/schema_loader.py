# app/schema_loader.py
import os
import json
from typing import List
from pathlib import Path
from pydantic import BaseModel

class SchemaDefinition(BaseModel):
    name: str
    fields: List[str]
    description: str
    required: List[str]

def load_all_schemas(schema_dir: str = "schemas") -> List[SchemaDefinition]:
    schema_list = []
    for file in os.listdir(schema_dir):
        if file.endswith(".json"):
            with open(Path(schema_dir) / file, "r", encoding="utf-8") as f:
                data = json.load(f)
                schema = SchemaDefinition(**data)
                schema_list.append(schema)
    return schema_list
