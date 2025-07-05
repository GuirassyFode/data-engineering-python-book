import streamlit as st
import mysql.connector
import pandas as pd

# Step 1: Connect to the MySQL database
def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",      # MySQL server host
        user="root",           # MySQL username
        password="Test123456",  # MySQL password
        database="dataengineerdb"  # Your database name
    )

# Step 2: Query the MySQL database
def get_data_from_mysql(query):
    connection = connect_to_mysql()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Step 3: Streamlit UI
def app():
    st.title("MySQL Data Viewer")

    st.markdown("""
    This is a simple Streamlit app that connects to a MySQL database and fetches data.
    """)

    # Input SQL query
    query = st.text_area("Enter SQL Query", "SELECT * FROM ratings LIMIT 5;")

    # Button to run the query
    if st.button("Run Query"):
        try:
            # Get data
            data = get_data_from_mysql(query)

            # Convert the data into a Pandas DataFrame
            df = pd.DataFrame(data, columns=["name", "rating", "region"])

            # Display the DataFrame
            st.write("### Results")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    app()
