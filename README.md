
# What-If Timeline Simulator

Imagine alternate histories. Simulate possible futures.  
**The What-If Timeline Simulator** uses a powerful AI agent to explore counterfactual scenarios like:

>  *"What if humans landed on Mars in 1999?"*  
>  *"What if the Cold War had gone nuclear?"*  
>  *"What if climate change was solved in 2020?"*

Built with LangChain + Hugging Face + Streamlit.

---

##  Features

-  **Agentic Reasoning** using LangChain's ReAct framework
-  **Web search tools** (DuckDuckGo) for fact-grounded scenarios
-  **Natural timeline generation** based on user input
-  **User-provided Hugging Face API key** (free-tier friendly)
-  **Deployable on Streamlit Cloud** for global access

---

##  Tech Stack

| Component | Tool |
|----------|------|
| LLM Agent | [LangChain ReAct Agent](https://docs.langchain.com/docs/components/agents/) |
| LLM Model | [`mistralai/Mixtral-8x7B-Instruct-v0.1`](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) via HF Inference API |
| Tool | [`DuckDuckGoSearchRun`](https://python.langchain.com/docs/integrations/tools/ddg_search) |
| UI | [Streamlit](https://streamlit.io) |
| Hosting | [Streamlit Cloud](https://streamlit.io/cloud) |
| Auth | User-supplied Hugging Face key (no backend auth needed)


---

## Directory Suggestion

```
what-if/
├── app.py
├── chains/
│   └── whatif_chain.py
├── config/
│   └── settings.py
├── requirements.txt
├── README.md  
└── .env.example  

```

## Installation

```bash
git clone https://github.com/knight22-21/what-if-agent.git
cd what-if
pip install -r requirements.txt
````

---

## Run Locally

Create a `.env` file only if you want to hardcode your Hugging Face key:

```env
HUGGINGFACEHUB_API_TOKEN=hf_...
```

Then run the app:

```bash
streamlit run app.py
```

OR, let users enter their API key at runtime in the UI.

---

## Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **New App** → Select repo + `app.py`
4. Add environment variables if needed (e.g. for your own demo key)

---

## Example Prompts

* What if humans landed on Mars in 1999?
* What if World War II never happened?
* What if AGI emerged in 2025?
* What if fossil fuels were banned in 2030?

---

## Credits

Created by **Krishna** ⚔️
Powered by [LangChain](https://www.langchain.com/), [Hugging Face](https://huggingface.co), and [Streamlit](https://streamlit.io)





