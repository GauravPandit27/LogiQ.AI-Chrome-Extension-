from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from constants import groq_key

# Step 1: Initialize Groq model
llm = ChatGroq(
    groq_api_key=groq_key,
    model_name="llama3-70b-8192",
    temperature=0
)

# Step 2: Prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You're an expert assistant. Analyze the user's question below and provide a clear answer.

Question: {question}
Answer:"""
)

# Step 3: Create the LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# Step 4: Expose function
def solve_question(question: str) -> str:
    return chain.run(question)

