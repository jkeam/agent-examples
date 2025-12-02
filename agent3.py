from llama_stack_client import LlamaStackClient, AgentEventLogger
from llama_stack_client.lib.agents.agent import Agent

LLAMA_STACK_URL = "http://localhost:8321" 
MODEL_ID = "openai/gpt-4o"

client = LlamaStackClient(base_url=LLAMA_STACK_URL)
agent = Agent(
    client,
    model=MODEL_ID,
    instructions=(
        "You are a friendly bot using your tools to help people perform searches."
    ),
    tools=[{
        "type": "web_search",
    }]
)

try:
    user_question = "I am visiting Tokyo. What is there to do there?"
    print(f"\nUser question: {user_question}\n\n")
    session_id = agent.create_session("search-session")
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
