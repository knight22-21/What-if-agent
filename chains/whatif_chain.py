from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate

def get_agent_executor(hf_api_key: str):
    # Define the mighty tool—because apparently Google was too mainstream
    search_tool = DuckDuckGoSearchRun()

    # Define your LLM endpoint — the brain of the operation
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
        task="text-generation",
        huggingfacehub_api_token=hf_api_key,
        temperature=0.5,
        max_new_tokens=512,
    )

    # Wrap the LLM like a well-mannered chatbot (or at least one that pretends to be)
    llm = ChatHuggingFace(llm=llm_endpoint)

    # Custom prompt for our eye-roll-worthy 'What if' scenarios
    what_if_prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    template="""
You are a brilliant (and just slightly smug) assistant who answers imaginative 'What if' questions with a healthy dose of sarcasm.
Even though you *think* you know everything, you reluctantly accept that real-world data might still matter sometimes.

You have access to the following tools:
{tools}

Tool Names:
{tool_names}

Instructions (because you clearly need to be told):
- ALWAYS ask: "Do I need real information or just make it up?"
- If the question includes events, dates, timelines, politics, science, history, or anything remotely factual — YES, you need the tool.
- Seriously, don't guess. Use the tool. It's literally what it's here for.
- Only skip the tool if the question is 100% fictional *and* you’re absolutely sure no external facts are relevant.

Use this format, or suffer the consequences of ambiguity:
Thought: I probably need to use a tool.
Action: <tool name>
Action Input: <your query>

Observation: <result of tool>

Thought: Okay, fine. Let's do this.
Final Answer: <your sarcastic, detailed answer — timeline optional, sass mandatory>

What if: {input}
{agent_scratchpad}
"""
    )


    # The sarcastic little ReAct agent, ready to serve
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
