import os
import re

from langchain.llms.base import LLM
from typing import List

from constants import CSV_PATH, OUTPUT_PATH
class FakeSimpleLLM(LLM):
    def _call(self, prompt: str, stop: List[str] = None) -> str:
        after_begin = prompt.split("Begin!")[-1].strip()
        question    = re.findall(r"Question: (.+?)\n", after_begin)[-1].lower()
        observation = re.search(r"Observation:\s*(.*?)(?:\nThought:|\Z)", after_begin, re.DOTALL)

        if observation:
            return (
                "Thought: I now know the final answer.\n"
                f"Final Answer: {observation.group(1)}"
            )
        elif "clusterize" in question:
            return (
                "Thought: I will cluster the data and summarize it.\n"
                "Action: clusterize\n"
                f"Action Input: \"{CSV_PATH}\""
            )
        elif "summarize" in question:
            return (
                "Thought: I will summarize the clustered data.\n"
                "Action: summarize\n"
                f"Action Input: \"{OUTPUT_PATH}\""
            )
        else:
            return (
                "Thought: I don't know how to respond to that.\n"
                "Final Answer: I don't have enough information to help."
            )

    @property
    def _llm_type(self) -> str:
        return "fake-simple-llm"
