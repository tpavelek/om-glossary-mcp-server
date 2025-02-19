from typing import Any, Dict, List

from mcp.types import Tool, TextContent

from src.openmetadata import OpenMetadataClient

LIST_TABLES_TOOL = Tool(
    name="list_tables",
    description="List tables from OpenMetadata",
    inputSchema={
        "type": "object",
        "properties": {
            "limit": {
                "type": "integer",
                "description": "Maximum number of tables to return",
                "default": 10
            },
            "offset": {
                "type": "integer",
                "description": "Number of tables to skip",
                "default": 0
            }
        }
    }
)

def list_all_tools() -> List[Tool]:
    return [LIST_TABLES_TOOL]


def call_tool(name: str, arguments: Dict[str, Any], client: OpenMetadataClient) -> List[TextContent]:
    if name == LIST_TABLES_TOOL.name:
        limit = arguments.get("limit", 10)
        offset = arguments.get("offset", 0)
        results = client.list_tables(limit=limit, offset=offset)
        return [TextContent(type="text", text=str(results))]
    else:
        raise ValueError(f"Unknown tool: {name}")
