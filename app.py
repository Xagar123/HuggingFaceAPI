from langchain.llms import HuggingFaceHub
import os
from getpass import getpass

os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass("HF Token:")

llm = HuggingFaceHub(
    repo_id="huggingfaceh4/zephyr-7b-alpha", 
    model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512}
)

# query = "Write a mail to my boss for 2 day leave"
query= input("enter ur promt")


prompt = f"""
 <|system|>
You are an AI assistant that follows instruction extremely well.
Please be truthful and give direct answers
</s>
 <|user|>
 {query}
 </s>
 <|assistant|>
"""

response = llm.predict(prompt)
print(response)