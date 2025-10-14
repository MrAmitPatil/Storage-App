import streamlit as st

st.set_page_config(layout="wide")

st.title('ModelGenie DOCUMENTATION')

st.header('Introduction')
st.markdown("""
The Generative Data Modeling Tool is an AI-powered application that automates the process of creating logical and physical data models from source files. It uses Snowflake Cortex to analyze uploaded data files and generate comprehensive data models, including ER diagrams and SQL DDL scripts.""")

st.header('Description')
st.subheader('Business Benefits:')
st.markdown("""
Data Quality and Cleansing
Organizations increasingly rely on large volumes of structured data across disparate files and sources. Manual data modeling is slow, error-prone, and resource-intensive — especially when reconciling naming anomalies, inferring schemas, or creating documentation.

The Generative Data Modeling Tool addresses these challenges by:

Accelerating data onboarding: Quickly converts raw CSV/Excel files into usable data models

Improving data quality: Detects schema inconsistencies and applies normalization rules

Reducing manual work: Automatically generates logical models, ERDs, and SQL scripts

Enhancing governance and reproducibility: Centralized, consistent modeling within Snowflake

Scaling data architecture: Enables quick prototyping and refinement for modern analytics

By operating entirely within the Snowflake ecosystem, it supports enterprise-scale data engineering workflows without moving data or relying on external AI services.
""")

st.header('Steps to Use')
st.subheader('Expected workflow for client specific outputs:')
st.markdown("""
Step 1: Upload Files
•	Click "Browse files" or drag-and-drop CSV/Excel files
•	Multiple files from the same business domain recommended
•	Use "Clear All Files" to reset selections
Step 2: Select Target Database
•	Choose from supported databases: Snowflake, SQL Server, Oracle, Redshift, Synapse
•	Selection affects generated DDL syntax
Step 3: Generate Model
•	Click "Generate Data Model" button
•	Processing time varies based on file size and complexity
•	Progress indicated by spinner animation
Step 4: Review Outputs
Overview Tab
•	Displays column profiling statistics
•	Shows data types, null percentages, distinct counts
•	Highlights uniqueness constraints
Logical Model Tab
•	Shows AI-generated logical data model
•	Identifies fact and dimension tables
•	Defines relationships and grain
ERD Tab
•	Visual entity-relationship diagram
•	Downloadable PNG format
•	Shows cardinalities and relationships
SQL DDL Tab
•	Complete CREATE TABLE statements
•	Primary and foreign key constraints
•	Database-specific syntax
•	Downloadable SQL file
SCD Tab
•	Slowly Changing Dimension recommendations
•	Type 1/2/3 rationales based on data profiling

""")

st.header('Example Prompts')
st.markdown("""
- You are a senior enterprise data modeler. 
You will analyze the provided table schemas and profiling results 
to design a logical dimensional data model.

CRITICAL RULES:
- Normalize column names (snake_case)
- Identify fact vs dimension tables
- Handle anomalies consistently (e.g., cust_id = customer_id)
- Always generate primary & foreign keys
- Ensure referential integrity
- Produce outputs in four labeled sections:
  LOGICAL_MODEL, ERD, DDL, SCD_RECOMMENDATIONS

TABLES_ROWCOUNT:
{table_rows_estimate}

SCHEMAS_BY_TABLE:
{schemas_by_table}

PROFILING_BY_TABLE:
{profiling_by_table}
 
""")

