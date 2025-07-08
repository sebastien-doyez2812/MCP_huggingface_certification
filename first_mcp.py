from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str)-> str:
    return f"Weather in {location}, Sunny, 32°C"

@mcp.ressource("weather://{location}")
def weather_ressource(location: str) -> str:
    return f"Weather in {location}, Sunny, 32°C"


@mcp.prompt()
def weather_report(location: str) -> str:
    return f"""You are a weather reporter. Weather report for {location}?"""


if __name__ == "__main__":
    mcp.run()