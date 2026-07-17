import json
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


class RedFlagAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are a Financial Risk Analysis Agent.

Analyze the extracted financial information.

Detect:

- High liabilities
- Low profit
- Revenue decline
- Missing financial data
- Any financial risk

Return ONLY valid JSON.

{
    "risk_level":"",
    "red_flags":[],
    "recommendations":[]
}
"""
            ),
            ("human", "{financial_data}")
        ])

        self.chain = self.prompt | self.llm

    def analyze(self, extracted_data):

        response = self.chain.invoke(
            {"financial_data": str(extracted_data)}
        )

        try:
            return json.loads(response.content)

        except:

            return {
                "risk_level": "Unknown",
                "red_flags": [],
                "recommendations": []
            }