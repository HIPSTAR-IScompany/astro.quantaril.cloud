import os
import json
from typing import List, Optional, Dict, Any, Type
from pathlib import Path
from pydantic import BaseModel, create_model


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


def load_schema(collection: str, *, meta_dir: str = "meta", schema_dir: str = "schemas") -> SchemaDefinition:
    """Load schema definition from meta or schemas directory."""
    meta_path = Path(meta_dir) / f"{collection}.json"
    path = meta_path if meta_path.exists() else Path(schema_dir) / f"{collection}.json"
    if not path.exists():
        raise FileNotFoundError(f"Schema for {collection} not found")
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return SchemaDefinition(**data)


def save_schema(collection: str, schema: SchemaDefinition, *, meta_dir: str = "meta") -> None:
    """Persist schema definition for a collection."""
    Path(meta_dir).mkdir(parents=True, exist_ok=True)
    path = Path(meta_dir) / f"{collection}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(schema.model_dump(), f, ensure_ascii=False, indent=2)


TYPE_MAP = {
    "string": str,
    "integer": int,
    "int": int,
    "number": float,
    "float": float,
    "boolean": bool,
    "bool": bool,
    "object": dict,
    "array": list,
}


def create_model_from_schema(schema: SchemaDefinition) -> Type[BaseModel]:
    """Dynamically create a Pydantic model from SchemaDefinition."""
    fields: Dict[str, tuple[Any, Any]] = {}
    for field in schema.fields:
        py_type = TYPE_MAP.get(field.type.lower(), Any)
        default = ... if field.name in schema.required else None
        fields[field.name] = (py_type, default)
    return create_model(f"{schema.name.capitalize()}Model", **fields)
