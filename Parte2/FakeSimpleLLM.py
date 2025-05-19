import os

from langchain.llms.base import LLM
from tools import output_path

csv_filename = 'iris_data_challenge.csv'
csv_path = os.path.join(os.path.dirname(os.getcwd()), csv_filename)

class FakeSimpleLLM(LLM):
    has_clustered: bool = False
    has_summarized: bool = False

    def _call(self, prompt, stop=None):
        if not self.has_clustered and "clusteriz" in prompt.lower():
            self.has_clustered = True
            return (
                "Thought: I will cluster the data and summarize it.\n"
                "Action: clusterize\n"
                f"Action Input: \"{csv_path}\""
            )
        elif not self.has_summarized and "summariz" in prompt.lower():
            self.has_summarized = True
            return (
                "Thought: I will summarize the clustered data.\n"
                "Action: summarize\n"
                f"Action Input: \"{output_path}\""
            )
        else:
            return (
                "Thought: I don't know how to respond to that.\n"
                "Final Answer: I don't have enough information to help."
            )

    @property
    def _llm_type(self) -> str:
        return "fake-simple-llm"
