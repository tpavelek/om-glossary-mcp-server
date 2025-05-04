from typing import Any, Dict, List

from mcp.types import TextContent, Tool

from src.openmetadata import OpenMetadataClient

LIST_TABLES_TOOL = Tool(
    name="list_tables",
    description="List tables from OpenMetadata",
    inputSchema={
        "type": "object",
        "properties": {
            "limit": {"type": "integer", "description": "Maximum number of tables to return", "default": 10},
            "offset": {"type": "integer", "description": "Number of tables to skip", "default": 0},
        },
    },
)

GET_TABLE_TOOL = Tool(
    name="get_table",
    description="Get details of a specific table by ID",
    inputSchema={
        "type": "object",
        "properties": {
            "table_id": {"type": "string", "description": "ID of the table to retrieve", "format": "uuid"},
            "fields": {
                "type": "string",
                "description": "Fields to include in the response",
                "example": "name,description,columns,tags,href",
            },
        },
        "required": ["table_id"],
    },
)

GET_TABLE_BY_NAME_TOOL = Tool(
    name="get_table_by_name",
    description="Get details of a specific table by fully qualified name",
    inputSchema={
        "type": "object",
        "properties": {
            "fqn": {"type": "string", "description": "Fully qualified name of the table"},
            "fields": {
                "type": "string",
                "description": "Fields to include in the response",
                "example": "name,description,columns,tags,href",
            },
        },
        "required": ["fqn"],
    },
)

CREATE_TABLE_TOOL = Tool(
    name="create_table",
    description="Create a new table",
    inputSchema={
        "type": "object",
        "properties": {
            "table_data": {"type": "object", "description": "Table data including name, description, columns, etc."},
        },
        "required": ["table_data"],
    },
)

UPDATE_TABLE_TOOL = Tool(
    name="update_table",
    description="Update an existing table",
    inputSchema={
        "type": "object",
        "properties": {
            "table_id": {"type": "string", "description": "ID of the table to update", "format": "uuid"},
            "table_data": {"type": "object", "description": "Updated table data"},
        },
        "required": ["table_id", "table_data"],
    },
)

DELETE_TABLE_TOOL = Tool(
    name="delete_table",
    description="Delete a table",
    inputSchema={
        "type": "object",
        "properties": {
            "table_id": {"type": "string", "description": "ID of the table to delete", "format": "uuid"},
            "hard_delete": {"type": "boolean", "description": "Whether to perform a hard delete", "default": False},
            "recursive": {"type": "boolean", "description": "Whether to recursively delete children", "default": False},
        },
        "required": ["table_id"],
    },
)

LIST_GLOSSARIES_TOOL = Tool(
    name="list_glossaries",
    description="List glossaries from OpenMetadata",
    inputSchema={
        "type": "object",
        "properties": {
            "limit": {"type": "integer", "description": "Maximum number of glossaries to return", "default": 10},
            "fields": {
                "type": "string",
                "description": "Fields to include in the returned resource",
                "example": "owners,tags,reviewers,usageCount,termCount,domain,extension",
            },
            "before": {"type": "string", "description": "Returns list of glossaries before this cursor"},
            "after": {"type": "string", "description": "Returns list of glossaries after this cursor"},
            "include": {
                "type": "string",
                "description": "Include all, deleted, or non-deleted entities.",
                "default": "non-deleted",
                "enum": ["all", "deleted", "non-deleted"],
            },
        },
    },
)

GET_GLOSSARY_BY_NAME_TOOL = Tool(
    name="get_glossary_by_name",
    description="Get details of a specific glossary by fully qualified name",
    inputSchema={
        "type": "object",
        "properties": {
            "fqn": {"type": "string", "description": "Fully qualified name of the glossary"},
            "fields": {
                "type": "string",
                "description": "Fields to include in the returned resource",
                "example": "owners,tags,reviewers,usageCount,termCount,domain,extension",
            },
            "include": {
                "type": "string",
                "description": "Include all, deleted, or non-deleted entities.",
                "default": "non-deleted",
                "enum": ["all", "deleted", "non-deleted"],
            },
        },
        "required": ["fqn"],
    },
)

# --- Glossary Term Tools ---

LIST_GLOSSARY_TERMS_TOOL = Tool(
    name="list_glossary_terms",
    description="List glossary terms from OpenMetadata, optionally filtered by glossary FQN.",
    inputSchema={
        "type": "object",
        "properties": {
            "glossary_fqn": {"type": "string", "description": "Fully qualified name of the glossary to filter terms from."},
            "limit": {"type": "integer", "description": "Maximum number of terms to return", "default": 10},
            "fields": {
                "type": "string",
                "description": "Fields to include in the returned resource",
                "example": "children,relatedTerms,reviewers,owners,tags,usageCount,domain,extension,childrenCount",
            },
            "before": {"type": "string", "description": "Returns list of terms before this cursor"},
            "after": {"type": "string", "description": "Returns list of terms after this cursor"},
            "include": {
                "type": "string",
                "description": "Include all, deleted, or non-deleted entities.",
                "default": "non-deleted",
                "enum": ["all", "deleted", "non-deleted"],
            },
        },
    },
)

GET_GLOSSARY_TERM_BY_NAME_TOOL = Tool(
    name="get_glossary_term_by_name",
    description="Get details of a specific glossary term by fully qualified name.",
    inputSchema={
        "type": "object",
        "properties": {
            "fqn": {"type": "string", "description": "Fully qualified name of the glossary term (e.g., 'GlossaryName.TermName')"},
            "fields": {
                "type": "string",
                "description": "Fields to include in the returned resource",
                "example": "children,relatedTerms,reviewers,owners,tags,usageCount,domain,extension,childrenCount",
            },
            "include": {
                "type": "string",
                "description": "Include all, deleted, or non-deleted entities.",
                "default": "non-deleted",
                "enum": ["all", "deleted", "non-deleted"],
            },
        },
        "required": ["fqn"],
    },
)

def list_all_tools() -> List[Tool]:
    return [
        LIST_TABLES_TOOL,
        GET_TABLE_TOOL,
        GET_TABLE_BY_NAME_TOOL,
        CREATE_TABLE_TOOL,
        UPDATE_TABLE_TOOL,
        DELETE_TABLE_TOOL,
        LIST_GLOSSARIES_TOOL,
        GET_GLOSSARY_BY_NAME_TOOL,
        LIST_GLOSSARY_TERMS_TOOL,
        GET_GLOSSARY_TERM_BY_NAME_TOOL,
    ]


def call_tool(name: str, arguments: Dict[str, Any], client: OpenMetadataClient) -> List[TextContent]:
    if name == LIST_TABLES_TOOL.name:
        limit = arguments.get("limit", 10)
        offset = arguments.get("offset", 0)
        results = client.list_tables(limit=limit, offset=offset)
        return [TextContent(type="text", text=str(results))]
    elif name == GET_TABLE_TOOL.name:
        table_id = arguments["table_id"]
        fields = arguments.get("fields")
        results = client.get_table(table_id=table_id, fields=fields)
        return [TextContent(type="text", text=str(results))]
    elif name == GET_TABLE_BY_NAME_TOOL.name:
        fqn = arguments["fqn"]
        fields = arguments.get("fields")
        results = client.get_table_by_name(fqn=fqn, fields=fields)
        return [TextContent(type="text", text=str(results))]
    elif name == CREATE_TABLE_TOOL.name:
        table_data = arguments["table_data"]
        results = client.create_table(table_data=table_data)
        return [TextContent(type="text", text=str(results))]
    elif name == UPDATE_TABLE_TOOL.name:
        table_id = arguments["table_id"]
        table_data = arguments["table_data"]
        results = client.update_table(table_id=table_id, table_data=table_data)
        return [TextContent(type="text", text=str(results))]
    elif name == DELETE_TABLE_TOOL.name:
        table_id = arguments["table_id"]
        hard_delete = arguments.get("hard_delete", False)
        recursive = arguments.get("recursive", False)
        client.delete_table(table_id=table_id, hard_delete=hard_delete, recursive=recursive)
        return [TextContent(type="text", text=f"Table {table_id} deleted successfully")]
    elif name == LIST_GLOSSARIES_TOOL.name:
        limit = arguments.get("limit", 10)
        fields = arguments.get("fields")
        before = arguments.get("before")
        after = arguments.get("after")
        include = arguments.get("include", "non-deleted")
        results = client.list_glossaries(limit=limit, fields=fields, before=before, after=after, include=include)
        return [TextContent(type="text", text=str(results))]
    elif name == GET_GLOSSARY_BY_NAME_TOOL.name:
        fqn = arguments["fqn"]
        fields = arguments.get("fields")
        include = arguments.get("include", "non-deleted")
        results = client.get_glossary_by_name(fqn=fqn, fields=fields, include=include)
        return [TextContent(type="text", text=str(results))]
    elif name == LIST_GLOSSARY_TERMS_TOOL.name:
        glossary_fqn = arguments.get("glossary_fqn")
        limit = arguments.get("limit", 10)
        fields = arguments.get("fields")
        before = arguments.get("before")
        after = arguments.get("after")
        include = arguments.get("include", "non-deleted")

        glossary_id_to_use = None
        if glossary_fqn:
            try:
                # Get the glossary ID using the FQN
                glossary_details = client.get_glossary_by_name(fqn=glossary_fqn, fields="id")
                glossary_id_to_use = glossary_details.get("id")
                if not glossary_id_to_use:
                    return [TextContent(type="text", text=f"Error: Could not find ID for glossary FQN '{glossary_fqn}'.")]
            except Exception as e:
                # Handle cases where glossary lookup fails (e.g., not found, API error)
                return [TextContent(type="text", text=f"Error looking up glossary '{glossary_fqn}': {e}")]

        # Call list_glossary_terms with the resolved ID (or None if no FQN provided)
        results = client.list_glossary_terms(
            glossary_id=glossary_id_to_use, limit=limit, fields=fields, before=before, after=after, include=include
        )
        return [TextContent(type="text", text=str(results))]
    elif name == GET_GLOSSARY_TERM_BY_NAME_TOOL.name:
        fqn = arguments["fqn"]
        fields = arguments.get("fields")
        include = arguments.get("include", "non-deleted")
        results = client.get_glossary_term_by_name(fqn=fqn, fields=fields, include=include)
        return [TextContent(type="text", text=str(results))]
    else:
        raise ValueError(f"Unknown tool: {name}")
