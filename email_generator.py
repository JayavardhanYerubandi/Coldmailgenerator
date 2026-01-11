from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
llm=ChatGroq(
    model_name="llama3-8b-8192",
    api_key="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",
)

loader=WebBaseLoader("https://apna.co/job/kolkata-calcutta/territory-sales-officer-539812014")
page_data=loader.load().pop().page_content

from langchain_core.prompts import PromptTemplate

prompt_extract = PromptTemplate.from_template(
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

chain_extract=prompt_extract | llm
res=chain_extract.invoke(input={'page_data':page_data})

json_parser=JsonOutputParser()
json_res=json_parser.parse(res.content)

import pandas as pd
df=pd.read_csv("my_portfolio.csv")

import chromadb
import uuid
client=chromadb.PersistentClient('vectorstore')
collection=client.get_or_create_collection(name="portfolio")
if not collection.count():
    for _, row in df.iterrows():
        collection.add(documents=[row["Techstack"]],
                       metadatas=[{"links": row["Links"]}],
                       ids=[str(uuid.uuid4())])
        
job=json_res

links=collection.query(query_texts=job['skills'], n_results=2).get('metadatas', [])
        
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

chain_email=prompt_email|llm
res=chain_email.invoke({"job_description": str(job), "link_list": links})
print(res.content)
