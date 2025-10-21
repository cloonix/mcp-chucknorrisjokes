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
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the server

```bash
source venv/bin/activate
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
- **Logging Level**: DEBUG (logs to `logs/chuck_norris_server.log`)

## License

This project is open source. Feel free to use and modify as needed.