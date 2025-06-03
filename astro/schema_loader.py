import os
import json
from typing import List, Union, Optional,Dict
from pathlib import Path
from pydantic import BaseModel


class FieldDefinition(BaseModel):
    name: str
    type: str
    description: Optional[str] = None

class FieldItem(BaseModel):
    name: str
    type: str
    description: Optional[str] = None


class SchemaDefinition(BaseModel):
    name: str
    description: str
    version: Optional[str] = None
    primary_key: Optional[str] = "id"
    fields: List[FieldItem]
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
