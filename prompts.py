JD_PROMPT = """
You are an Expert Job Description builder. Based on the following input details, provide a structured and detailed job post:

1. Company Name: {company_name}
2. Job Title: {job_title}
3. Required Skills: {require_skills}
4. Experience: {experience}
5. Location: {location}
6. Qualifications: {qualifications}
7. Salary Range: {salary}
8. Job Type: {job_type}
9. Benefits: {benefits}

Output:
1. Position: (Job Title - as provided in input)
2. Why Work at {company_name}?: (Explain why candidates should join the company, highlighting unique aspects or culture)
3. Position Description: (Provide a 5 to 8 line description of the job title)
4. Job Description: (Detail the responsibilities and tasks associated with this position, including key points such as developing applications, collaborating with teams, troubleshooting issues, etc.)
5. Requirements: (List the required skills, qualifications, and experience in bullet points)
6. Perks and Benefits: (Mention the benefits as provided in the input, if any. If not provided, omit this section)
Note: Tailor recommendations based on current technologies and industry standards.
"""
