from llama_stack_client import LlamaStackClient, AgentEventLogger
from llama_stack_client.lib.agents.agent import Agent

LLAMA_STACK_URL = "http://localhost:8321" 
MODEL_ID = "openai/gpt-4o"

def get_current_weather(city: str) -> str:
    """
    A tool that returns the current weather in Celsius for a specified city. Use this FIRST to get weather data.

    :param city: The name of the city to find the weather for. This parameter is required.
    """
    if city.lower() == "tokyo":
        # Simulate a tool response
        return "Weather data for Tokyo: The temperature is 18°C and it is cloudy."
    if city.lower() == "miami":
        return "Weather data for Miami: The temperature is 30°C and it is sunny."
    return "Weather data could not be found for that city."

def recommend_outfit(weather_data: str) -> str:
    """
    A tool that analyzes a weather data string and provides an appropriate clothing recommendation. Use this SECOND.

    :param weather_data: The weather data to find the recommended outfit for. This parameter is required.
    """
    if "30°C" in weather_data or "sunny" in weather_data:
        return "Based on the warm and sunny weather, I recommend light clothing, shorts, and sunglasses."
    if "18°C" in weather_data or "cloudy" in weather_data:
        return "Based on the mild and cloudy weather, I recommend a light jacket and comfortable walking shoes."
    return "The weather is too unpredictable; I recommend layers."


client = LlamaStackClient(base_url=LLAMA_STACK_URL)
agent = Agent(
    client,
    model=MODEL_ID,
    instructions=(
        "You are a friendly bot using your tools to help people figure out what to wear based on the weather."
    ),
    tools=[get_current_weather, recommend_outfit],
)


try:
    user_question = "I am visiting Tokyo. What should I wear today?"
    print(f"\nUser question: {user_question}\n\n")
    session_id = agent.create_session("recommend-clothes-session")
    response = agent.create_turn(
        messages=[
            {"role": "user", "content": user_question}
        ],
        session_id=session_id
    )
    for log in AgentEventLogger().log(response):
        print(log, end="")
except Exception as e:
    print(f"An error occurred: {e}")
