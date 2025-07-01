import streamlit as st
from chains.whatif_chain import agent_executor

st.set_page_config(
    page_title="What-If Simulator",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("# 🌍 What-If Timeline Simulator")
st.markdown("Ask *counterfactual history* questions and explore alternate timelines using AI.")

# Input box
user_input = st.text_area("🔮 What if...", placeholder="e.g., What if the Cold War turned into a nuclear conflict in 1962?", height=100)

# Button to trigger agent
if st.button("Generate Timeline") and user_input.strip() != "":
    with st.spinner("Generating alternate timeline..."):
        try:
            response = agent_executor.invoke({"input": user_input})
            st.markdown("## 🧭 Timeline")
            st.markdown(response["output"])
        except Exception as e:
            st.error(f"Something went wrong: {e}")
else:
    st.caption("Enter a scenario and click the button to begin.")
