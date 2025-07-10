from mcp.server.fastmcp import FastMCP

# create an MCP server
mcp = FastMCP('Weather Service')  # service's name


# tool implementation
@mcp.tool()
def get_weather(location: str) -> str:
    """get the current weather for a specified location."""
    return f"weather in {location}: sunny, 72°F"


# resource implementation
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """provide weather data as a resource."""
    return f"weather data for {location}: sunny, 72°F"


# prompt implementation
@mcp.prompt()
def weather_report(location: str) -> str:
    """create a weather report prompt."""
    return f"you are a weather reporter. weather report for {location}?"


if __name__ == '__main__':
    mcp.run()
