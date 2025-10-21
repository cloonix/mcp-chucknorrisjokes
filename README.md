# Chuck Norris MCP Server

A Model Context Protocol (MCP) server that provides access to Chuck Norris jokes from the [Chuck Norris API](https://api.chucknorris.io).

## Features

- **Random Jokes**: Get random Chuck Norris jokes via MCP tool
- **Error Handling**: Robust error handling for API failures and network issues
- **Logging**: Comprehensive logging for debugging and monitoring

## Prerequisites

- Python 3.8 or higher

## Installation

1. **Clone or download this repository**

2. **Set up virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the server

```bash
source .venv/bin/activate
python3 server.py
```

The server will start and listen for MCP protocol messages on stdin/stdout.

### API Reference

#### `get_random_joke`
Fetches a random Chuck Norris joke from the API.

**Parameters**: None

**Returns**: A string containing the joke text.

## Configuration

- **API Base URL**: `https://api.chucknorris.io/jokes`
- **Timeout**: 10 seconds for API requests
- **Logging Level**: INFO (use `--debug` flag for DEBUG level, logs to `logs/chuck_norris_server.log`)

## Integration with MCP Clients

### Claude Desktop

Add the following to your `claude_desktop_config.json` (typically located at `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "chuck-norris": {
      "command": "python3",
      "args": ["/path/to/your/mcp-chucknorris/server.py"],
      "env": {
        "PATH": "/path/to/your/mcp-chucknorris/.venv/bin:$PATH"
      }
    }
  }
}
```

Replace `/path/to/your/mcp-chucknorris` with the actual path to your project directory.

### Claude Code (VSCode Extension)

In your VSCode `settings.json`, add:

```json
{
  "claude-code.mcpServers": {
    "chuck-norris": {
      "command": "python3",
      "args": ["server.py"],
      "cwd": "/path/to/your/mcp-chucknorris"
    }
  }
}
```

### Kilo Code (VSCode Extension)

In your VSCode `settings.json`, add:

```json
{
  "kilo-code.mcpServers": {
    "chuck-norris": {
      "command": "python3",
      "args": ["server.py"],
      "cwd": "/path/to/your/mcp-chucknorris"
    }
  }
}
```

### GitHub Copilot in VSCode

If using an MCP-enabled extension for GitHub Copilot, add to your VSCode `settings.json`:

```json
{
  "github.copilot.mcpServers": {
    "chuck-norris": {
      "command": "python3",
      "args": ["server.py"],
      "cwd": "/path/to/your/mcp-chucknorris"
    }
  }
}
```

## License

This project is open source. Feel free to use and modify as needed.