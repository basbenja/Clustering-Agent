import os
import re

from langchain_core.language_models.llms import LLM
from tools import output_path

csv_filename = 'iris_data_challenge.csv'
csv_path = os.path.join(os.path.dirname(os.getcwd()), csv_filename)

class FakeSimpleLLM(LLM):
    def _call(self, prompt, stop=None):
        questions = re.findall(r"Question: (.+?)\n", prompt)
        question = questions[-1]

        if "clusterize" in question.lower():
            return (
                "Thought: I will cluster the data and summarize it.\n"
                "Action: clusterize\n"
                f"Action Input: \"{csv_path}\""
            )
        elif "summarize" in question.lower():
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
