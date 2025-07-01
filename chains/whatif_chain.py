from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

search_tool = DuckDuckGoSearchRun()

llm_endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation",
    temperature=0.5,
    max_new_tokens=512,
)

llm = ChatHuggingFace(llm=llm_endpoint)

# ✅ Updated PromptTemplate with required input variables
what_if_template = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    template="""You are a highly creative and logical assistant who answers hypothetical 'What if' questions.
Your task is to explore the scenario in a thoughtful, step-by-step, and imaginative way.

Available Tools:
{tools}

Tool Names:
{tool_names}

Instructions:
- If necessary, use tools to find facts.
- Think step-by-step.
- Be imaginative, but grounded in reasoning.

Format:
Thought: Do I need to use a tool?
Action: <tool name>
Action Input: <your query>

Thought: Proceeding with analysis...
Final Answer: <your detailed 'what if' scenario>

What if: {input}
{agent_scratchpad}
"""
)

agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=what_if_template
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True,
    handle_parsing_errors=True
)

response = agent_executor.invoke({"input": "What if humans never discovered fire?"})

print("\n--- What If Response ---\n")
print(response["output"])
