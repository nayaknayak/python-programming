
import streamlit as st
import pandas as pd

from sql_generator import generate_sql
from sql_executor import execute_sql


st.set_page_config(
    page_title="AI SQL Query Assistant",
    page_icon="🗄️",
    layout="wide"
)

st.title("🗄️ AI SQL Query Assistant")
st.write(
    "Ask questions about your employee database "
    "in natural language."
)

question = st.text_input(
    "Enter your question",
    placeholder="Example: Find the top 3 highest-paid employees"
)

if st.button("Generate SQL and Execute", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        try:
            with st.spinner("Generating SQL with Gemini..."):
                sql_query = generate_sql(question)

            st.subheader("Generated SQL")
            st.code(sql_query, language="sql")

            with st.spinner("Executing SQL query..."):
                results = execute_sql(sql_query)

            st.subheader("Query Results")

            if results:
                df = pd.DataFrame(results)
                st.dataframe(df, use_container_width=True)
                st.success(f"Retrieved {len(df)} row(s).")

            else:
                st.info(
                    "No results returned, or the query "
                    "could not be executed. Check your "
                    "terminal for errors."
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")

