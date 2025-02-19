from typing import Any, Dict, Optional

import httpx


class OpenMetadataError(Exception):
    """Base exception for OpenMetadata client errors."""
    pass


class OpenMetadataClient:
    """Client for interacting with OpenMetadata API."""
    
    def __init__(self, host: str, api_token: Optional[str] = None, username: Optional[str] = None, password: Optional[str] = None):
        """Initialize OpenMetadata client.
        
        Args:
            host: OpenMetadata host URL
            api_token: API token for authentication
            username: Username for basic auth
            password: Password for basic auth
            
        Raises:
            OpenMetadataError: If neither API token nor username/password is provided
        """
        self.host = host.rstrip('/')
        self.session = httpx.Client()
        
        # Set up authentication
        if api_token:
            self.session.headers['Authorization'] = f'Bearer {api_token}'
        elif username and password:
            # Basic auth implementation would go here
            pass
        else:
            raise OpenMetadataError("Either API token or username/password must be provided")

    def list_tables(self, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
        """List tables with pagination.
        
        Args:
            limit: Maximum number of tables to return
            offset: Number of tables to skip
            
        Returns:
            Dictionary containing table list and metadata
            
        Raises:
            OpenMetadataError: If the API request fails
        """
        response = self.session.get(
            f"{self.host}/api/v1/tables",
            params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        return response.json()

    def get_table(self, table_id: str) -> Dict[str, Any]:
        """Get details of a specific table.
        
        Args:
            table_id: ID of the table
            
        Returns:
            Table details
            
        Raises:
            OpenMetadataError: If the API request fails
        """
        response = self.session.get(f"{self.host}/api/v1/tables/{table_id}")
        response.raise_for_status()
        return response.json()

    def create_table(self, table_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new table.
        
        Args:
            table_data: Table data
            
        Returns:
            Created table details
            
        Raises:
            OpenMetadataError: If the API request fails
        """
        response = self.session.post(f"{self.host}/api/v1/tables", json=table_data)
        response.raise_for_status()
        return response.json()

    def update_table(self, table_id: str, table_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing table.
        
        Args:
            table_id: ID of the table to update
            table_data: Updated table data
            
        Returns:
            Updated table details
            
        Raises:
            OpenMetadataError: If the API request fails
        """
        response = self.session.put(f"{self.host}/api/v1/tables/{table_id}", json=table_data)
        response.raise_for_status()
        return response.json()

    def delete_table(self, table_id: str) -> None:
        """Delete a table.
        
        Args:
            table_id: ID of the table to delete
            
        Raises:
            OpenMetadataError: If the API request fails
        """
        response = self.session.delete(f"{self.host}/api/v1/tables/{table_id}")
        response.raise_for_status() 
