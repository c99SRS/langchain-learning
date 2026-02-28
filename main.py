import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


load_dotenv()



def main():
    print("Hello from langchain-course!")
    #print(os.getenv("OPENAI_API_KEY"))
    information ="what is the capital of France?"
    summary_template = """
    Given the following information: {information}
    1.search the capital of france
    2.what is the population of france
    3.what is the language of france
    4.what is the currency of france
    5.what is the religion of france
    6.what is the government of france
    7.what is the history of france
    8.what is the culture of france
    9.what is the art of france
    10.what is the music of france
    """
    summary_prompt = PromptTemplate(template=summary_template, input_variables=["information"])
    
    #llm = ChatOpenAI(model="gpt-5", temperature=0)
    llm = ChatOllama(temperature=0, model="gemma3:270m")

    
    chain = summary_prompt | llm
    response = chain.invoke({"information": information})
    print(response.content)



if __name__ == "__main__":
    main()


