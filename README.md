📧 AI-Powered Cold Email Generator

An AI-powered Cold Email Generator that creates personalized, professional outreach emails using LLMs and vector-based semantic search.
Instead of sending generic templates, this system generates context-aware cold emails by matching job or company requirements with relevant portfolio projects.

This project demonstrates a real-world implementation of Retrieval-Augmented Generation (RAG) using modern AI tooling.

✨ Key Features

✅ Generates custom cold emails based on job descriptions or company context

✅ Uses semantic similarity search to retrieve relevant portfolio projects

✅ Produces non-generic, personalized emails grounded in real data

✅ Modular, clean, and easy-to-extend codebase

✅ Suitable for job applications, internships, and professional outreach

🧠 Project Overview

Cold emailing often fails due to lack of personalization.
This project solves that problem by combining:

Large Language Models (LLMs) for natural language generation

Embeddings + Vector Database for semantic matching

Portfolio-aware context injection to improve relevance

The result is a ready-to-send professional cold email tailored to the opportunity.

🔄 How It Works

Portfolio data is stored in a CSV file

Portfolio entries are converted into embeddings

Embeddings are stored in a ChromaDB vector store

Job description or company details are given as input

Relevant portfolio projects are retrieved using semantic similarity

An LLM generates a context-aware cold email using retrieved data

🛠 Tech Stack

Python

LangChain

Large Language Models (OpenAI-compatible)

ChromaDB (Vector Database)

Embeddings for Semantic Search

CSV-based Portfolio Data

Environment Variables (.env)

📂 Project Structure
cold_email_generator/
│
├── app/
│   ├── main.py              # Main application entry point
│   ├── chains.py            # Prompt templates and LLM chains
│   ├── portfolio.py         # Portfolio loading and processing
│   ├── utils.py             # Utility/helper functions
│   ├── resources/
│   │   └── my_portfolio.csv # Portfolio dataset
│   └── vectorstore/         # ChromaDB persistent storage
│
├── email_generator.py       # Standalone email generation script
├── my_portfolio.csv         # Portfolio CSV file
└── vectorstore/             # Vector database files

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/cold-email-generator.git
cd cold-email-generator

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the root directory and add your API key:

OPENAI_API_KEY=your_api_key_here

5️⃣ Run the Application
python app/main.py

📌 Example Use Cases

Job applications

Internship outreach

Freelance proposals

Networking emails

Recruiter or startup outreach

🎯 Learning Outcomes

Hands-on experience with Retrieval-Augmented Generation (RAG)

Working with vector databases and embeddings

Prompt engineering and LLM chaining

Designing a real-world AI productivity tool

Structuring scalable and modular Python projects

🚧 Limitations

Designed for learning and portfolio use, not production-scale deployment

API costs depend on LLM usage

Email tone depends on prompt quality and input clarity

🔮 Future Improvements

Web-based UI (Streamlit / Django / React)

Multiple email tone options (formal, friendly, concise)

Support for multiple portfolio files

Email performance tracking

Integration with email clients

📄 Disclaimer

This project is intended for educational and portfolio demonstration purposes only.
Not optimized for commercial or large-scale production use.

👤 Author

Jayavardhan
B.Tech CSE Student
