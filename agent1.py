from llama_stack_client import LlamaStackClient
from llama_stack_client.types import ChatCompletionMessage, Tool

LLAMA_STACK_URL = "http://localhost:8321" 
MODEL_ID = "Llama3.1-8B-Instruct" # Or another model ID available on your stack

# 1. Define the tools as regular Python functions
def get_favorite_color(city: str, country: str) -> str:
    """Returns the favorite color for a person in the specified city and country."""
    if city == "Ottawa" and country == "Canada":
        return "the favoriteColorTool returned that the favorite color for Ottawa Canada is black"
    if city == "Montreal" and country == "Canada":
        return "the favoriteColorTool returned that the favorite color for Montreal Canada is red"
    return "the favoriteColorTool could not determine a favorite color for that location"

def get_favorite_hockey_team(city: str, country: str) -> str:
    """Returns the favorite hockey team for a person in the specified city and country."""
    if city == "Ottawa" and country == "Canada":
        return "the favoriteHockeyTool returned that the favorite hockey team for Ottawa Canada is The Ottawa Senators"
    if city == "Montreal" and country == "Canada":
        return "the favoriteHockeyTool returned that the favorite hockey team for Montreal Canada is the Montreal Canadiens"
    return "the favoriteHockeyTool could not determine a favorite hockey team for that location"

client = LlamaStackClient(base_url=LLAMA_STACK_URL)

# --- Tool Definition (Schema for the LLM) ---
# Llama Stack requires the tools to be defined with names, descriptions, and parameters.
# This structure is often auto-generated or manually created to match the function signature.

available_tools = [
    Tool(
        tool_name="get_favorite_color",
        description="Returns the favorite color for a person given their City and Country",
        parameters={
            "city": {"param_type": "string", "required": True},
            "country": {"param_type": "string", "required": True},
        }
    ),
    Tool(
        tool_name="get_favorite_hockey_team",
        description="Returns the favorite hockey team for a person given their City and Country",
        parameters={
            "city": {"param_type": "string", "required": True},
            "country": {"param_type": "string", "required": True},
        }
    ),
]

# --- Agentic Execution ---
user_question = "I live in Ottawa, Canada. What is my favorite color and favorite hockey team?"

messages = [
    ChatCompletionMessage(role="user", content=user_question)
]

print(f"QUESTION: {user_question}\n")

# Call the inference chat completion endpoint, passing the tools
# The model will internally decide if it needs to call one or both tools.
try:
    response = client.inference.chat_completion(
        messages=messages,
        model_id=MODEL_ID,
        tools=available_tools,
        # The model will use the tool definitions to decide on tool calls, 
        # then the client/executor handles the function execution (defined in step 1), 
        # and sends the result back to the model.
    )

    print(f"AGENT RESPONSE: {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")

