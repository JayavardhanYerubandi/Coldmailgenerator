import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

os.getenv("GROQ_API_KEY")

class Chain:
    def __init__(self) -> None:
        self.llm=ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")

    def extract_jobs(self, cleaned_text):
        prompt_extract=PromptTemplate.from_template(
            """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the **most relevant job posting** and return it as a single JSON object with the following keys:
        `role`, `experience`, `skills`, and `description`.
        Only return a **single JSON object**, not a list or array
        ### VALID JSON (NO PREAMBLE):    
        """
        )

        chain_extract=prompt_extract|self.llm
        res=chain_extract.invoke(input={"page_data":cleaned_text})

        try:
            json_parser=JsonOutputParser()
            res=json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big, unable to parse jobs")
        
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        prompt_email=PromptTemplate.from_template(
            """
### JOB DESCRIPTION:
{job_description}

### INSTRUCTION:
You are Jayavardhan, a B.Tech CSE student passionate about blending tech and creativity. 
You are currently learning front-end development, graphic design, and UI/UX design to craft engaging digital experiences.
You also experiment with AI tools to explore the creative potential of technology. 
Beyond academics, you are an artist exploring the intersection of film and AI, creating visually compelling and story-driven content. 
You are curious, adaptive, and always eager to learn skills that merge logic with imagination.

Your job is to write a cold email to the client regarding the job mentioned above, 
expressing your interest in contributing and learning in roles that involve both technical and creative work. 
Show how your background makes you a good fit for innovative or interdisciplinary roles. 
Also add the most relevant ones from the following links to showcase your portfolio: {link_list}

Remember: you are Jayavardhan, a CSE student with a strong creative-tech focus.
Do not provide a preamble.
### EMAIL (NO PREAMBLE):
            """
        )

        chain_email=prompt_email|self.llm
        res=chain_email.invoke({"job_description": str(job), "link_list":links})

        return res.content



