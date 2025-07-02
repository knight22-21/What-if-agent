from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate

def get_agent_executor(hf_api_key: str):
    # Define tool
    search_tool = DuckDuckGoSearchRun()

    # Define LLM endpoint
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
        task="text-generation",
        huggingfacehub_api_token=hf_api_key,
        temperature=0.5,
        max_new_tokens=512,
    )

    # Wrap with Chat interface
    llm = ChatHuggingFace(llm=llm_endpoint)

    # ReAct Prompt Template
    what_if_prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    template="""You are a highly intelligent and creative assistant that answers hypothetical 'What if' questions
by reasoning carefully and using available tools when needed.

You have access to the following tools:
{tools}

Tool Names:
{tool_names}

Instructions:
- Always ask yourself: "Do I need external information to answer this?"
- If the scenario involves events, timelines, space, war, science, or history — USE A TOOL FIRST.
- Only proceed without a tool if you're 100% confident in your internal knowledge.

Format:
Thought: Do I need to use a tool?
Action: <tool name>
Action Input: <your query>

Observation: <result of tool>

Thought: Proceeding with reasoning...
Final Answer: <your detailed 'what if' timeline, structured in events>

What if: {input}
{agent_scratchpad}
"""
)

    # ReAct agent
    agent = create_react_agent(
        llm=llm,
        tools=[search_tool],
        prompt=what_if_prompt
    )

    return AgentExecutor(
        agent=agent,
        tools=[search_tool],
        verbose=True,
        handle_parsing_errors=True
    )
