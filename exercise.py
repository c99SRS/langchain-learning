from email import message
import os
from pyexpat import model

from langchain_core.prompts import prompt
from openai.types.responses import response


class ChatGroq:

    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = ["llama-4-8binstant",
                            "llama-3.3-70b-versatile",
                            "llama-3.1-8b-instant"
                            ]
        if model not in self.valid_models:
            raise ValueError(f"Invalid model: {model}. Valid models are: {self.valid_models}")
    
    def invoke(self, messages):
        if not isinstance(messages, list) or len(messages) == 0:
            raise ValueError("Messages must be a non-empty list")
        
        #simulate different responses from the model
        if self.model == "llama-4-8binstant":
            content = f"[Lalama 4 response] Machine leanrning is a subset of artificial intelligence that focuses on creating algorithms that can learn from data and make predictions or decisions without being explicitly programmed."
        elif self.model == "llama-3.3-70b-versatile":
            content = f"[Lalama 3.3 response] Machine leanrning is like teaching a computer to recognize pattern in data, much like how humanlearn from experience. The key difference is that machines can learn from vast amounts of data, much faster than humans."
        elif self.model == "llama-3.1-8b-instant":
            content = f"[Lalama 3.1 response] Machine leanrning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content = f"[Mock response] This is simulated response from the {self.model} model."

        return MockAIMessage(content)
        

class MockAIMessage:
    def __init__(self, content):
        self.content = content

def implement_set_api_key(api_key):
        """ Implement: set the GROQ_API_KEY environment variable.
            Args:
              api_key: str - the API key to use for the Groq API
         """
        os.environ["GROQ_API_KEY"] = api_key
        print("API key has been set in environment variables!")

def check_api_key():
        """ Check if GROQ_API_KEY is set in environment variables.
            Raise exception if not set """

        if "GROQ_API_KEY" not in os.environ:
            raise ValueError("GROQ_API_KEY environent variable is required.")
    
def implement_llama_4_model():
        """
        Implement: Create and return a chatGroq instance for llama4. 
        Use the exact model name from console.groq.com
        set temperature=0 for consistent response
        """
        return ChatGroq(model="llama-4-8b-instant", temperature=0, max_retries=2)
    
def implement_llama_3_3_model():
        """
        Implement: Create and return a chatGroq instance for llama 3.3. 
        Use the exact model name from console.groq.com
        set slighlty more creartive response
        """
        return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3, max_retries=2)
    
def implement_query_model(model, prompt):
        """
        Implement: Send a query to the model and return the response content.
        Args:
            model: The ChatGroq model instance
            prompt: The text prompt to send

        Rerurn :
           str: The response content
        """
        try:
            messages = [("human", prompt)]
            response = model.invoke(messages)
            return response.content

        except Exception as e:
            raise Exception(f"Error querying model: {str(e)}")


def main():
        """ Main function to test your implementation """

        print("Groq model switching exercise. (Langchain Integration)")
        print("Thise exercise simulates langchain-groq package behaviour!")
        print("Model names should match console.groq.com exactly")
        print()

        try:
            print("Setting API key...")
            implement_set_api_key("mock_api_key_for_testing")
            check_api_key()
            print("api key validation working!")

            #Test prompt
            test_prompt = "Explain the concept of machine learning in 1 sentence"
            print(f"Testing llama 4 implementation:")
            llama4 = implement_llama_4_model()
            response4 = implement_query_model(llama4, test_prompt)
            print(f"Lama 4: {response4}\n")

            print(f"Testing llama 3.3 implementation:")
            llama33 = implement_llama_3_3_model()
            response33 = implement_query_model(llama33, test_prompt)
            print(f"Lama 3.3: {response33}\n")

            print("All implementation working!")
            print("Great job implementing the Langchain-Groq patterns")
        except Exception as e:
            if "GROQ_API_KEY" in str(e):
                print("\n Chekc ur implementation_set_api_key() function!")
            else:
                print("Chekc ur function implementation!")
                print("verify model name match console.groq.com exzctly")



if __name__ == "__main__":
    main()  

       

