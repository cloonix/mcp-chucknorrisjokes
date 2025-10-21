#!/usr/bin/env python3
"""
Chuck Norris MCP Server

A Model Context Protocol server that provides access to Chuck Norris jokes
from the Chuck Norris API (https://api.chucknorris.io).
"""

import argparse
import asyncio
import json
import logging
import os
import sys
from typing import Any, Sequence

import requests
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)

# Parse command line arguments
parser = argparse.ArgumentParser(description="Chuck Norris MCP Server")
parser.add_argument('--debug', action='store_true', help='Enable debug logging')
args = parser.parse_args()

# Configure logging
log_level = logging.DEBUG if args.debug else logging.INFO
log_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(log_dir, 'logs', 'chuck_norris_server.log')
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler(log_file)
    ]
)
logger = logging.getLogger("chuck-norris-server")

# API Configuration
CHUCK_NORRIS_API_BASE = "https://api.chucknorris.io/jokes"

class ChuckNorrisServer:
    """MCP Server for Chuck Norris jokes."""

    def __init__(self):
        self.server = Server("chuck-norris-server")

    async def get_random_joke(self) -> str:
        """Fetch a random Chuck Norris joke from the API."""
        logger.info("Fetching random joke from Chuck Norris API...")
        try:
            logger.debug(f"Making GET request to: {CHUCK_NORRIS_API_BASE}/random")
            response = requests.get(f"{CHUCK_NORRIS_API_BASE}/random", timeout=10)
            logger.debug(f"API Response Status: {response.status_code}")
            logger.debug(f"API Response Headers: {dict(response.headers)}")
            response.raise_for_status()
            data = response.json()
            logger.debug(f"API Response Data: {json.dumps(data, indent=2)}")
            joke = data.get("value", "No joke found")
            logger.info(f"Successfully fetched joke: {joke[:50]}...")
            return joke
        except requests.RequestException as e:
            logger.error(f"Failed to fetch joke: {e}")
            raise RuntimeError(f"Failed to fetch Chuck Norris joke: {str(e)}")
        except ValueError as e:
            logger.error(f"Invalid JSON response: {e}")
            raise RuntimeError("Invalid response from Chuck Norris API")

    async def handle_get_random_joke(self, arguments: dict[str, Any]) -> list[TextContent]:
        """Handle the get_random_joke tool call."""
        logger.info(f"Handling get_random_joke tool call with arguments: {json.dumps(arguments, indent=2)}")
        try:
            joke = await self.get_random_joke()
            logger.info(f"Returning joke to client: {joke[:50]}...")
            return [TextContent(type="text", text=joke)]
        except RuntimeError as e:
            logger.error(f"Error in get_random_joke handler: {e}")
            return [TextContent(type="text", text=f"Error: {str(e)}")]

    async def setup_tools(self):
        """Set up the available tools."""
        logger.info("Setting up MCP tools...")

        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            logger.debug("Client requested tool list")
            tools = [
                Tool(
                    name="get_random_joke",
                    description="Get a random Chuck Norris joke",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                )
            ]
            logger.info(f"Returning {len(tools)} tools to client")
            return tools

        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
            logger.info(f"Client called tool: {name}")
            if name == "get_random_joke":
                return await self.handle_get_random_joke(arguments)
            else:
                logger.error(f"Unknown tool requested: {name}")
                raise ValueError(f"Unknown tool: {name}")

    async def run(self):
        """Run the MCP server."""
        await self.setup_tools()
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )

async def main():
    """Main entry point."""
    logger.info("Initializing Chuck Norris MCP Server...")
    server = ChuckNorrisServer()
    logger.info("Starting Chuck Norris MCP Server...")
    try:
        await server.run()
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user")
    except Exception as e:
        logger.error(f"Server crashed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())