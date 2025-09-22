import streamlit as st

st.set_page_config(layout="wide")

st.title('Customer Churn Propensity')

st.header('Introduction')
st.markdown("""
The churn prediction app leverages Snowflake and Streamlit, utilizing advanced machine learning algorithms to analyze customer behavior and identify patterns that may indicate potential churn. 

The Streamlit-based interface ensures user-friendly interactions, catering to both data professionals and business stakeholders. This app empowers organizations to make informed decisions and optimize their customer retention efforts.
""")

st.header('Features included')
st.markdown("""
1. Churn Propensity:
- Compute churn probability score for all the customers under selection.
 
2. Churn Classification:
- Classify churn probability score into High, Medium and Low.
 
3. Feature Weights:
- Provide weights and directions for model attributes.
 
4. Model Explanability:
- Provide model Explanability to understand the computation of churn probability at each customer level.
 
5. Multi-Business Sector:
- The Customer Churn Propensity model may be used for mutiple business sectors (Banking, Insurance, Financial Services etc.).
""")

st.header('Description')
st.subheader('Business Benefits:')
st.markdown("""
- Early identification of customers at high risk of attrition.
 
- Devise strategy to retain customer at high risk of attrition.
 
- Customer retention.
 
- Sustainable growth in customer base.
 
- Continuous growth in business revenue.
""")

st.subheader('Expected workflow for client specific outputs:')
st.markdown("""
- The client does not have to handle any development activities as it is entirely handled by the NSEIT team.

- Consumer data are kept private and secure. After the app is installed, it is recommended by the provider to grant the following privileges as needed.
""")

st.header('Steps to Use')
st.markdown("""
1. Variable/Feature Description:

    * CreditScore: Represents the credit score of the customer.
    * Geography: Indicates the geographical location of the customer.
    * Gender: Denotes the gender of the customer.
    * Age: Represents the age of the customer.
    * Tenure: Denotes the number of years the customer has been associated with the bank.
    * Balance: Represents the account balance of the customer.
    * NumOfProducts: Indicates the number of products (e.g., banking products) the customer has with the bank.
    * HasCrCard: Indicates whether the customer has a credit card (1 for Yes, 0 for No).
    * IsActiveMember: Denotes whether the customer is an active member (1 for Yes, 0 for No).
    * EstimatedSalary: Represents the estimated salary of the customer.
   
2. It is mandatory to keep same column names to run this app successfully.

3. Customer can initiate the process by installing the churn prediction application directly from the Snowflake Marketplace, ensuring a seamless integration into their existing Snowflake environment.

4. Customer can then grant select and insert access to the specific tables/views containing scoring data and final results with columns matching the following definitions:

    * scoring_data:

        * customer_id (varchar(100))
        * creditscore (number(10,0))
        * geography (varchar(1000))
        * gender (varchar(100))
        * age (number(5,0))
        * tenure (number(5,0))
        * balance (number(28,10))
        * numofproducts (number(10,0))
        * hascrcard (number(1,0))
        * isactivemember (number(1,0))
        * estimatedsalary (number(28,10))
    
    * final_result:

        * customer_id (varchar(100))
        * creditscore (number(10,0))
        * geography (varchar(1000))
        * gender (varchar(100))
        * age (number(5,0))
        * tenure (number(5,0))
        * balance (number(28,10))
        * numofproducts (number(10,0))
        * hascrcard (number(1,0))
        * isactivemember (number(1,0))
        * estimatedsalary (number(28,10))
        * probability (number(28,10))
        * churn_category (varchar(20))

5. Customer can start using the application for customer churn prediction.
""")

st.header('Sample Queries')
code = '''Select CUSTOMER_ID,PROBABILITY,CHURN_CATEGORY
from final_result'''
st.code(code, language='sql')