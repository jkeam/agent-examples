from llama_stack_client import LlamaStackClient
from llama_stack_client.types import ChatCompletionMessage, Tool

# Assuming a Llama Stack server is running (same as the previous example)
LLAMA_STACK_URL = "http://localhost:8321" 
MODEL_ID = "Llama3.1-8B-Instruct" 

# 1. Define the tools as regular Python functions
def get_current_weather(city: str) -> str:
    """Returns the current weather in a given city in Celsius."""
    if city.lower() == "tokyo":
        # Simulate a tool response
        return "Weather data for Tokyo: The temperature is 18°C and it is cloudy."
    if city.lower() == "miami":
        return "Weather data for Miami: The temperature is 30°C and it is sunny."
    return "Weather data could not be found for that city."

def recommend_outfit(weather_data: str) -> str:
    """Analyzes weather data (string) and returns a clothing recommendation."""
    if "30°C" in weather_data or "sunny" in weather_data:
        return "Based on the warm and sunny weather, I recommend light clothing, shorts, and sunglasses."
    if "18°C" in weather_data or "cloudy" in weather_data:
        return "Based on the mild and cloudy weather, I recommend a light jacket and comfortable walking shoes."
    return "The weather is too unpredictable; I recommend layers."

client = LlamaStackClient(base_url=LLAMA_STACK_URL)

# --- Tool Definition (Schema for the LLM) ---
# The definitions tell the LLM how and when to use the functions.

available_tools = [
    Tool(
        tool_name="get_current_weather",
        description="A tool that returns the current weather in Celsius for a specified city. Use this FIRST to get weather data.",
        parameters={
            "city": {"param_type": "string", "required": True},
        }
    ),
    Tool(
        tool_name="recommend_outfit",
        description="A tool that analyzes a weather data string and provides an appropriate clothing recommendation. Use this SECOND.",
        parameters={
            "weather_data": {"param_type": "string", "required": True},
        }
    ),
]

# --- Agentic Execution ---
user_question = "I am visiting Tokyo. What should I wear today?"

messages = [
    ChatCompletionMessage(role="user", content=user_question)
]

print(f"QUESTION: {user_question}\n")

try:
    # We call chat_completion with the tools. The model handles the multi-step chain internally.
    response = client.inference.chat_completion(
        messages=messages,
        model_id=MODEL_ID,
        tools=available_tools,
    )

    print(f"AGENT RESPONSE: {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
