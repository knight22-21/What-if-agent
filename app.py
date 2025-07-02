import streamlit as st
from chains.whatif_chain import get_agent_executor

st.set_page_config(
    page_title="What-If Simulator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 What-If Timeline Simulator")
st.markdown("Ask *counterfactual history* questions and explore alternate timelines using AI.")

# --- Hugging Face Key Input ---
user_api_key = st.text_input(
    "🔑 Enter your Hugging Face API Key (starts with hf_...)", 
    type="password", 
    placeholder="hf_..."
)

if not user_api_key:
    st.warning("You must provide a valid Hugging Face API key to use this simulator.")
    st.stop()

# --- Load agent dynamically ---
@st.cache_resource
def get_executor_cached(api_key: str):
    return get_agent_executor(api_key)

agent_executor = get_executor_cached(user_api_key)

# --- Usage Limit Config ---
MAX_QUERIES = 5
if "query_count" not in st.session_state:
    st.session_state.query_count = 0

# --- Input Section ---
user_input = st.text_area(
    "🧠 What if...", 
    placeholder="e.g. What if the Cold War turned into a nuclear war in 1962?", 
    height=100
)

if user_input:
    st.caption(f"Queries used: {st.session_state.query_count}/{MAX_QUERIES}")

# --- Timeline Generation ---
if st.button("Generate Timeline"):
    if st.session_state.query_count >= MAX_QUERIES:
        st.error("⚠️ Limit reached for this session. Please refresh to reset.")
    else:
        with st.spinner("Simulating alternate history..."):
            try:
                result = agent_executor.invoke({"input": user_input})
                st.markdown("## 🧭 Alternate Timeline")
                st.markdown(result["output"])
                st.session_state.query_count += 1
            except Exception as e:
                st.error(f"❌ Error: {e}")