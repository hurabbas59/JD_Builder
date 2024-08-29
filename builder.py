import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts import JD_PROMPT

# Prompt template
prompt_template = JD_PROMPT

prompt = PromptTemplate(
    template=prompt_template, 
    input_variables=[
        "company_name", "job_title", "require_skills", "experience", 
        "location", "qualifications", "salary", 
        "job_type", "benefits"
    ]
)

OPENAI_API_KEY = ''
 
llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY,temperature = 0.7)
chain = prompt | llm | StrOutputParser()

def main():
    print("Job Description Builder")

    try:
        company_name = input("Company name: ")
        job_title = input("Job Title: ")
        require_skills = input("Required Skills: ")
        experience = input("Experience: ")
        location = input("Location: ")
        qualifications = input("Qualifications: ")
        salary = input("Salary: ")
        job_type = input("Job Type: ")
        benefits = input("Benefits: ")

        user_inputs = {
            "company_name": company_name,
            "job_title": job_title,
            "require_skills": require_skills,
            "experience": experience,
            "location": location,
            "qualifications": qualifications,
            "salary": salary,
            "job_type": job_type,
            "benefits": benefits,
        }
        
        response = chain.invoke(user_inputs)
        
        # Output text is directly parsed
        output_text = response
        
        # Split the output into sections
        sections = output_text.split("\n\n")
        
        # Initialize empty strings for each section
        position_description = ""
        Job_description = ""
        Requirements = ""
        why_work_here = ""
        perks_and_benefits = ""

        # Extract relevant sections into the corresponding variables
        for section in sections:
            if "Position:" in section:
                position_description = section
            elif "Job Description:" in section:
                Job_description = section
            elif "Requirements:" in section:
                Requirements = section
            elif "Why Work at" in section:
                why_work_here = section
            elif "Perks and Benefits:" in section:
                perks_and_benefits = section
        
        # Display each section separately
        # print("Position Description:")
        print(position_description)

        # print("\nWhy Work Here:")
        print(why_work_here)
        
        # print("\nWhat You Will Do:")
        print(Job_description)
        
        # print("\nWhat You Bring:")
        print(Requirements)
        # 

        
        if perks_and_benefits:
            print("\nPerks and Benefits:")
            print(perks_and_benefits)
        
        # Retu rn each section separately
        return position_description,why_work_here, Job_description, Requirements, perks_and_benefits
        
    except ValueError:
        print("Invalid input, please ensure all inputs are correctly formatted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    result = main()
    if result is not None:
        position_description, Job_description, Requirements, why_work_here, perks_and_benefits = result
