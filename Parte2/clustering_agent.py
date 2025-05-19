from langchain.agents import initialize_agent, AgentType

from tools import clusterize, summarize
from FakeSimpleLLM import FakeSimpleLLM


fake_llm = FakeSimpleLLM()
tools = [clusterize, summarize]

agent = initialize_agent(
    tools=tools,
    llm=fake_llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    max_iterations=1,
)


def interactive_loop():
    print("\n======Starting interactive agent. Type 'exit' or 'quit' to stop.======\n")

    while True:
        user_input = input("👤 User: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting.")
            break

        try:
            output = agent.invoke(user_input)
            print(f"🤖 Agent: {output}\n")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    interactive_loop()
