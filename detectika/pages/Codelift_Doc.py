import streamlit as st

st.set_page_config(layout="wide")

st.title('CODELIFT DOCUMENTATION')

st.header('Introduction')
st.markdown("""
Nusummit brings the power of AI-assisted SQL migration directly to your Snowflake account with CodeLift.
Built using Streamlit and Snowpark, and powered by Snowflake Cortex, CodeLift enables seamless translation of SQL scripts from legacy databases such as MSSQL, Oracle, and PostgreSQL — without transferring files or sharing data outside your Snowflake Data Cloud.

Using advanced large language models through Snowflake Cortex, CodeLift automatically converts SQL code into your desired target dialect — including Snowflake, Redshift, or Databricks — while ensuring syntactic correctness, performance optimization, and functional integrity.

The intuitive Streamlit interface allows users to upload multiple SQL files, and download the converted scripts as a ZIP package — all within a secure Snowflake-native environment.
""")

st.header('Description')
st.subheader('Business Benefits:')
st.markdown("""
Time Efficiency – Automates tedious SQL conversions that would take weeks if done manually.
            
Reduced Errors – AI ensures consistent syntax conversion and reduces human mistakes.
            
Scalability – Can process hundreds of queries/files at once.
            
Cost Savings – Reduces dependency on large manual migration teams.
            
Future-Ready – Designed for multi-dialect support (Snowflake, Oracle, MySQL, DB2, Teradata, etc.).
            
Transparency – Maintains logs for traceability and auditing.
            
Ease of Use – Simple Streamlit UI for technical and non-technical users.
            
Accelerates Cloud Adoption – Helps enterprises migrate databases faster to modern platforms like Snowflake.
""")

st.header('Steps to Use')
st.subheader('Expected workflow for client specific outputs:')
st.markdown("""
• Customer installs the CodeLift application from the Snowflake Marketplace.
            
• Customer grants the required imported privileges to enable access to Snowflake services
            
    ↳ GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO APPLICATION Codelift;
            
• The customer launches the Streamlit UI, which comes pre-loaded with a sample SQL script to demonstrate the translation workflow and interface.
            
• Customer uploads SQL files (e.g., DDL, stored procedures) written in a source database dialect such as SQL Server, Oracle, or PostgreSQL.
            
• Customer selects a target database (e.g., Snowflake, Redshift, Databricks) for conversion.
            
• The application uses Snowflake Cortex AI to intelligently translate the uploaded SQL into the target dialect, handling syntax, functions, and procedural logic.
            
• Customer downloads a ZIP file containing all converted scripts for integration or further testing.
""")

st.header('Sample Queries')
st.markdown("""
- The below query uses the Snowflake Database's CORTEX.COMPLETE() function. 
""")
code = '''
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'claude-3-5-sonnet',
    $$You are an expert SQL developer. 
    Convert the following Microsoft SQL Server CREATE TABLE statement into Snowflake-compatible SQL.
    Ensure the output follows Snowflake best practices.

    <task>
    CREATE TABLE [dbo].[Employees] (
        EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
        FirstName NVARCHAR(50),
        LastName NVARCHAR(50),
        HireDate DATETIME DEFAULT GETDATE()
    );
    </task>

    Provide only the converted Snowflake SQL code inside a SQL code block.
    $$
) AS CONVERTED_SQL;
'''
st.code(code, language='sql')