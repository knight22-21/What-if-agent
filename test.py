from chains.whatif_chain import whatif_agent, prompt

scenario = "What if the Berlin Wall never fell?"
formatted = prompt.format({"scenario": scenario})

# One-shot analysis
response = whatif_agent.invoke(formatted)
print(response)

# Multi-turn conversation flows
followup = "Could you calculate population growth if it remained divided?"
res2 = whatif_agent.invoke(followup)
print(res2)
