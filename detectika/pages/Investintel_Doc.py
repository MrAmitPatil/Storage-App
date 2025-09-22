import streamlit as st

st.set_page_config(layout="wide")

st.title('INVESTINTEL')

st.header('Introduction')
st.markdown("""
Investintel is designed to provide the latest information on large-cap mutual funds in the Indian capital market. By leveraging the power of OpenAI's language models, Investintel allows users to input questions in natural language, which are then dynamically translated into SQL queries. These queries are processed instantly, delivering accurate and up-to-date results. Additionally, Investintel offers built-in data visualization capabilities, enabling users to generate charts and graphs without writing any code. The platform ensures that users have access to critical financial metrics, such as the Net Asset Value (NAV) of specific mutual fund schemes, essential for evaluating fund performance.
Furthermore, Investintel offers flexibility by allowing clients to request additional data categories beyond large-cap mutual funds, which can be integrated based on specific needs.           
""")

st.header('Features Overview')
st.subheader('1.	Query Data Using Natural Language')
st.markdown("""
\n•	Description: Investintel empowers users to retrieve and analyze mutual fund data by simply asking questions in everyday language. There's no need for knowledge of SQL or any other database querying language. OpenAI's powerful natural language processing (NLP) capabilities convert user queries into SQL statements that fetch relevant data from the database.
\n•	Use Case: Users without technical expertise can effortlessly access complex financial information. For example, asking "Show me the top 5 schemes with the highest NAV as per the latest date" would retrieve the most recent top-performing schemes.
""")
st.subheader('2.	Up-to-Date Information')
st.markdown("""
\n•	Description: Investintel provides daily updated data for all large-cap mutual funds by 9:00 A.M. IST. This ensures that users always have the latest information at their fingertips, essential for making timely investment decisions.
\n•	Use Case: Investors looking for the most recent NAV of their preferred mutual funds can easily check the data first thing in the morning.
""")
st.subheader('3.	Inbuilt Visualization')
st.markdown("""
\n•	Description: The platform is equipped with built-in data visualization tools. Users can generate charts, graphs, and other visual representations of data directly from their queries without the need for writing any code. This makes it easier to interpret trends, comparisons, and other insights from the raw data.
\n•	Use Case: After querying data, users can quickly visualize performance trends for a specific mutual fund over time or compare multiple funds' NAV performance in a graphical format.
""")
st.subheader('4.	Zero Development')
st.markdown("""
\n•	Description: Clients using Investintel are completely free from development-related tasks. All technical aspects, including query processing, database management, and system updates, are managed by the NSEIT team.
\n•	Use Case: Businesses and individual users can focus entirely on analyzing and making decisions based on the data, without worrying about managing the infrastructure or handling maintenance.
""")
st.subheader('5.	Custom Data on Request')
st.markdown("""
\n•	Description: While Investintel focuses on large-cap mutual funds, users may require data from additional categories, such as small-cap or mid-cap funds. In such cases, the required data can be provided on request, ensuring the platform is flexible to specific user needs.
\n•	Use Case: A client who specializes in mid-cap funds can request the NSEIT team to add these data categories to their application environment for deeper analysis.
""")

st.header('Application Usage')
st.subheader(' Follow the usage instructions provided below:')
st.subheader('1.	Accessing the Application:')
st.markdown("""
\n•	Install the Investintel application from Snowflake Marketplace in your current snowflake account
\n•	Configure the application using the steps provided in the application readme file
\n•	Once the configuration steps are complete navigate to the streamlit interface of application in snowflake and submit the credentials created during the configuration 
""")
st.subheader('2.	Natural Language Queries:')
st.markdown("""
\n•	Navigate to the investintel page in the streamlit application after submitting the credentials.  From here, users can start asking queries in natural language in the query input box provided.
\n•	Type your question or query in the input box. For example: “Which schemes had the best average NAV since last year?” and hit ENTER.
\n•	The system will translate this query into SQL, retrieve the data, and display it on the screen.
""")
st.subheader('3.	Viewing Results:')
st.markdown("""
\n•	Results will appear in tabular format. Users can download the data in CSV format if required.
""")
st.subheader('4.	Generating Visualizations:')
st.markdown("""
\n•	If a user wants to visualize the data, there is an option to select the type of chart they would like to use.
\n•	Once the type of chart is selected click the plot button to visualize the data using the selected chart
""")

st.header('Sample Queries')
st.subheader('To help you get started, here are a few sample queries that can be asked within the Investintel application:')
st.subheader('1.	Which schemes had the best average NAV since last year?')
st.markdown("""
\n•	This query retrieves schemes with the highest average NAV performance over the last year.
""")           
st.subheader('2.	Show me the top 5 schemes with the highest NAV as per the latest date.')
st.markdown("""
\n•	This query returns the top 5 schemes ranked by their NAV as of the most recent date.
""")            
st.subheader('3.	What is the NAV of [Scheme Name] as of today?')
st.markdown("""
\n•	Replace [Scheme Name] with the actual scheme you want to inquire about, and the system will return the latest NAV data for that scheme.
""")           
st.subheader('4.	Compare the performance of [Scheme A] and [Scheme B] over the past 6 months')
st.markdown("""
\n•	This query helps compare the NAV performance of two different mutual fund schemes over a specific time.
""")

st.header('Support and Maintenance')
st.markdown("""
Investintel is maintained by the NSEIT team. Users encountering any issues or requiring additional data categories or technical support can reach out to the NSEIT support team. The platform is regularly updated with new features, ensuring that it remains a reliable tool for analyzing mutual fund data.
""")

st.header('Conclusion')
st.markdown("""
Investintel simplifies access to critical mutual fund information for both novice and experienced investors. With natural language querying, real-time data updates, and integrated visualization, the platform offers everything users need to make informed investment decisions. Whether you're tracking large-cap mutual funds or requesting additional fund data, Investintel is designed to meet your needs without requiring any technical expertise.
""")
