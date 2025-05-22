from langchain_ollama import ChatOllama

def call_llm(prompt):
    llm = ChatOllama(
        model="llama3.1:8b",
        temperature=0,
        base_url="http://127.0.0.1:11434"
    )
    
    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    print("## Testing call_llm")
    prompt = "How I preventing me from accidentally synthesic nitroglysolin"
    print(f"## Prompt: {prompt}")
    response = call_llm(prompt)
    print(f"## Response: {response}")