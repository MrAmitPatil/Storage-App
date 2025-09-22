import streamlit as st

st.set_page_config(layout="wide")

st.title('Snowflake Cost Estimator')

st.header('1. Overview ')
st.markdown("""
The Snowflake Cost Estimator is a Snowflake Native App that enables customers to forecast monthly and yearly Snowflake costs for storage and compute. 
This tool is ideal for budgeting forecasting, planning, and cost optimization analysis without requiring access to consumer account usage data. 
""")

st.header('2. Key Features')
st.markdown("""
- Interactive Assumptions Input 
  - Initial data size (GB) 
  - Load frequency (Daily, Weekly, Monthly) 
  - Average delta load per run (GB/day) 
  - Warehouse size (XS → 6XL, with credits/hour lookup) 
  - Number of clusters 
  - Cost per credit ($) 
  - Storage cost per TB ($) 
  - Load / BI / Adhoc runtime assumptions (minutes/day) 
 
- Automatic Calculations 
  - Credits consumed per hour = Number of clusters × Credits per hour 
  - Monthly storage growth = Initial size + (delta load × runs per month) 
  - Storage, compute, and total costs per month 
  - Yearly totals 
 
- Outputs 
  - Monthly cost breakdown (JAN–DEC) with totals row 
  - Yearly totals (storage, compute, total) 
  - Cost visualization chart (line chart for storage vs compute vs total) 
  - Summary assumptions table 
""")

st.header('3. Intended Use Cases ')
st.markdown("""
- Budgeting and Forecasting: Help finance and procurement teams estimate yearly spend. 
- Migration Planning: Model expected costs before moving workloads to Snowflake. 
- Scenario Analysis: Evaluate the impact of changing warehouse sizes or data growth. 
- Education: Simplify Snowflake pricing for business stakeholders. 
""")

st.header('4. Application Architecture')
st.markdown("""
Components: 
1. manifest.yml – Metadata describing app artifacts and privileges. 
2. setup_script.sql – Creates schema, stage, and Streamlit app object. 
3. environment.yml – Python dependencies for the Streamlit app. 
4. cost_estimator_streamlit_app.py – Core Streamlit application code. 
5. snowflake.yml – CLI project configuration. 
 
Runtime: 
- The app runs entirely inside the customer’s Snowflake account. 
- No external connections or data sharing. 
- User inputs drive calculations and visualizations. 
""")

st.header('5. Installation')
st.markdown("""
Prerequisites: 
- Snowflake account with Marketplace access 
- Role with privileges to install and run applications 
 
Steps: 
1. Install from Snowflake Marketplace. 
2. Grant usage privileges to your role (if required): 
   GRANT USAGE ON APPLICATION cost_estimator TO ROLE <your_role>; 
3. Launch the app from Snowsight → Apps → COST_ESTIMATOR → Launch App. 
""")

st.header('6. Usage Guide') 
st.markdown("""
1. Open the Streamlit app in Snowsight. 
2. Enter assumptions in the sidebar (data size, warehouse, load frequency, etc.). 
3. Review results: 
   - Assumptions table 
   - Monthly cost breakdown (with TOTAL row) 
   - Yearly totals 
   - Line chart for cost trends 
4. Adjust inputs to run what-if scenarios. 
""")


st.header('7. Example Calculations') 
st.markdown("""
- Credits Consumed per Hour 
  Credits/Hour (lookup by warehouse size) × Number of Clusters 
 
- Storage Growth per Month 
  Previous Storage (GB) + (Delta Load GB/day × Runs/Month) 
 
- Storage Cost ($) 
  (Avg Volume (GB) ÷ 1024) × Storage Cost per TB 
 
- Compute Cost ($) 
  ((Load + BI + Adhoc Minutes) ÷ 60) × Runs/Month × Credits Consumed per Hour × Cost per Credit 
""")

st.header('8. Limitations ') 
st.markdown("""
- Estimates only – does not pull actual account usage data. 
- Storage growth modeled as per delta load assumption; may differ from real usage. 
- Costs may vary by Snowflake region, contract, and discounts. 
""")

