# mcp-server-openmetadata

A Model Context Protocol (MCP) server implementation for OpenMetadata, enabling seamless integration with MCP clients. This project provides a standardized way to interact with OpenMetadata through the Model Context Protocol.

## About

This project implements a [Model Context Protocol](https://modelcontextprotocol.io/introduction) server that wraps OpenMetadata's REST API, allowing MCP clients to interact with OpenMetadata in a standardized way.

## Feature Implementation Status

| Feature | API Path | Status |
|---------|----------|--------|
| **Metadata Assets** | | |
| List Tables | `/api/v1/tables` | ❌ |
| Get Table Details | `/api/v1/tables/{table_id}` | ❌ |
| Create Table | `/api/v1/tables` | ❌ |
| Update Table | `/api/v1/tables/{table_id}` | ❌ |
| Delete Table | `/api/v1/tables/{table_id}` | ❌ |
| **Database Services** | | |
| List Database Services | `/api/v1/services/databaseServices` | ❌ |
| Get Database Service | `/api/v1/services/databaseServices/{service_id}` | ❌ |
| Create Database Service | `/api/v1/services/databaseServices` | ❌ |
| Update Database Service | `/api/v1/services/databaseServices/{service_id}` | ❌ |
| Delete Database Service | `/api/v1/services/databaseServices/{service_id}` | ❌ |
| **Tags & Classifications** | | |
| List Classifications | `/api/v1/classifications` | ❌ |
| Get Classification | `/api/v1/classifications/{classification_id}` | ❌ |
| Create Classification | `/api/v1/classifications` | ❌ |
| Update Classification | `/api/v1/classifications/{classification_id}` | ❌ |
| Delete Classification | `/api/v1/classifications/{classification_id}` | ❌ |
| **Lineage** | | |
| Get Entity Lineage | `/api/v1/lineage/{entity_id}` | ❌ |
| Add Lineage Edge | `/api/v1/lineage` | ❌ |
| Delete Lineage Edge | `/api/v1/lineage/{from_id}/{to_id}` | ❌ |
| **Quality** | | |
| List Test Suites | `/api/v1/testSuites` | ❌ |
| Get Test Suite | `/api/v1/testSuites/{test_suite_id}` | ❌ |
| Create Test Suite | `/api/v1/testSuites` | ❌ |
| Update Test Suite | `/api/v1/testSuites/{test_suite_id}` | ❌ |
| Delete Test Suite | `/api/v1/testSuites/{test_suite_id}` | ❌ |
| **Glossary** | | |
| List Glossaries | `/api/v1/glossaries` | ❌ |
| Get Glossary | `/api/v1/glossaries/{glossary_id}` | ❌ |
| Create Glossary | `/api/v1/glossaries` | ❌ |
| Update Glossary | `/api/v1/glossaries/{glossary_id}` | ❌ |
| Delete Glossary | `/api/v1/glossaries/{glossary_id}` | ❌ |

## Setup

### Environment Variables

Set one of the following authentication methods:

#### Token Authentication (Recommended)
```
OPENMETADATA_HOST=<your-openmetadata-host>
OPENMETADATA_API_TOKEN=<your-api-token>
```

#### Basic Authentication
```
OPENMETADATA_HOST=<your-openmetadata-host>
OPENMETADATA_USERNAME=<your-username>
OPENMETADATA_PASSWORD=<your-password>
```

### Usage with Claude Desktop

Add to your `claude_desktop_config.json` using one of the following authentication methods:

#### Token Authentication (Recommended)
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uvx",
      "args": ["mcp-server-openmetadata"],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_API_TOKEN": "your-api-token"
      }
    }
  }
}
```

#### Basic Authentication
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uvx",
      "args": ["mcp-server-openmetadata"],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_USERNAME": "your-username",
        "OPENMETADATA_PASSWORD": "your-password"
      }
    }
  }
}
```

Alternative configuration using `uv`:

#### Token Authentication (Recommended)
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-openmetadata",
        "run",
        "mcp-server-openmetadata"
      ],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_API_TOKEN": "your-api-token"
      }
    }
  }
}
```

#### Basic Authentication
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-openmetadata",
        "run",
        "mcp-server-openmetadata"
      ],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_USERNAME": "your-username",
        "OPENMETADATA_PASSWORD": "your-password"
      }
    }
  }
}
```

Replace `/path/to/mcp-server-openmetadata` with the actual path where you've cloned the repository.

### Manual Execution

You can also run the server manually:
```bash
python src/server.py
```

Options:
- `--port`: Port to listen on for SSE (default: 8000)
- `--transport`: Transport type (stdio/sse, default: stdio)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
