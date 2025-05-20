import os

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

from constants import OUTPUT_PATH
from tools import clusterize, summarize
from FakeSimpleLLM import FakeSimpleLLM

fake_llm = FakeSimpleLLM()

tools = [
    Tool(
        name="clusterize",
        func=clusterize,
        description="Clusters the data in the given CSV file and returns a summary of the first few rows.",
    ),
    Tool(
        name="summarize",
        func=summarize,
        description="Summarizes the clustered data in the CSV file.",
    ),
]

agent = initialize_agent(
    tools=tools,
    llm=fake_llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
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
            print(f"🤖 Agent: {output['output']}\n")
        except Exception as e:
            print(f"Error: {e}")

    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)


if __name__ == "__main__":
    interactive_loop()
