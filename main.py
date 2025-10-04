from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp=FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers.
    Args:
        a (int): First number.
        b (int): Second number.
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

# Tool: Generate a random number within a range
@mcp.tool
def random_number(min: int, max: int) -> int:
    """Generate a random number within a specified range.
    Args:
        min (int): Minimum value.
        max (int): Maximum value.
    Returns:
        int: A random number between min and max.
    """
    return random.randint(min, max)


# Resource: Provide server information
@mcp.resource("info://server")
def server_info() -> str:
    """Provide information about the server.
    Returns:
        str: A JSON string containing server information.
    """
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A server that provides simple calculator functions.",
        "tools" : ["add", "random_number"],
        "author": "Abhijeet Samal"
    }
    return json.dumps(info, indent=4)

# Start the FastMCP server
if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)