from secret_key import api_key_client
import os
os.environ["OPENAI_API_KEY"] = api_key_client
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate    
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Initialize the model
llm = OpenAI(temperature=0.6)

def generate_business_idea(company_type):
    
    # 1. Chain to generate company name
    prompt_template_name = PromptTemplate(
        input_variables=["company_type"],
        template="I wanted to open a small {company_type} company in my city. Suggest me only one good name for it."   
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key="company_name"  # Add output_key
    )

    # 2. Chain to generate investment details
    prompt_template_investment_resources = PromptTemplate(
        input_variables=["company_name"],
        template="What initial investment and resources do we need for {company_name}?"   
    )

    company_investment_resources_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_investment_resources,
        output_key="investment_details"  # Add output_key
    )
    # Combine chains sequentially
    chain = SequentialChain(
        chains=[name_chain, company_investment_resources_chain],
        input_variables=["company_type"],
        output_variables=["company_name", "investment_details"],  # Include all outputs
        verbose=True
    )
    response = chain({"company_type": company_type})
    return response