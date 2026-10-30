import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model= 'gemini-3-flash-preview',
    google_api_key =  os.getenv('GOOGLE_API_KEY'),
    temperature = 0
)


DB_SCHEMA = """
Table: employees
Columns:
- employee_id (INT, primary key)
- employee_name (VARCHAR)
- salary (DECIMAL)
- department_id (INT, foreign key)
- joining_date (DATE)

Table: departments
Columns:
- department_id (INT, primary key)
- department_name (VARCHAR)
"""

# Instructions for generating SQL
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an SQL query generator for a MySQL database.

Use only the tables and columns provided in the schema.
Generate a single read-only SELECT query.
Do not generate INSERT, UPDATE, DELETE, DROP, or ALTER statements.
Return only the SQL query, without Markdown formatting.

Database schema:
{schema}
"""),("human", "{question}")
])

# Build the LangChain pipeline
chain = prompt | llm | StrOutputParser()

def generate_sql(question):
    sql_query = chain.invoke({
        "schema": DB_SCHEMA,
        "question": question
    })

    return sql_query.strip()


if __name__ == "__main__":
    question = "Find the top 3 highest-paid employees"

    sql_query = generate_sql(question)

    print("Generated SQL:")
    print(sql_query)


