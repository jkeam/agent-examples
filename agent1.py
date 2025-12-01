from llama_stack_client import LlamaStackClient, AgentEventLogger
from llama_stack_client.lib.agents.agent import Agent

LLAMA_STACK_URL = "http://localhost:8321" 
MODEL_ID = "openai/gpt-4o"

# Define the tools as regular Python functions
def get_favorite_color(city: str, country: str) -> str:
    """
    Returns the favorite color for a person given their City and Country.

    :param city: The name of the city. This parameter is required.
    :param country: The country the city is in. This parameter is required.
    """
    if city == "Ottawa" and country == "Canada":
        return "the favoriteColorTool returned that the favorite color for Ottawa Canada is black"
    if city == "Montreal" and country == "Canada":
        return "the favoriteColorTool returned that the favorite color for Montreal Canada is red"
    return "the favoriteColorTool could not determine a favorite color for that location"

def get_favorite_hockey_team(city: str, country: str) -> str:
    """
    Returns the favorite hockey team for a person given their City and Country.

    :param city: The name of the city. This parameter is required.
    :param country: The country the city is in. This parameter is required.
    """
    if city == "Ottawa" and country == "Canada":
        return "the favoriteHockeyTool returned that the favorite hockey team for Ottawa Canada is The Ottawa Senators"
    if city == "Montreal" and country == "Canada":
        return "the favoriteHockeyTool returned that the favorite hockey team for Montreal Canada is the Montreal Canadiens"
    return "the favoriteHockeyTool could not determine a favorite hockey team for that location"

client = LlamaStackClient(base_url=LLAMA_STACK_URL)
agent = Agent(
    client,
    model=MODEL_ID,
    instructions=(
        "You are a friendly bot using your tools to find favorite colors and hockey teams."
    ),
    tools=[get_favorite_color, get_favorite_hockey_team],
)

try:
    user_question = "I live in Ottawa, Canada. What is my favorite color and favorite hockey team?"
    print(f"\nUser question: {user_question}\n\n")
    session_id = agent.create_session("colorteam-session")
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

