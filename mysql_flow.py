import openai
import json
from mysql_class import Mysql
import os
from dotenv import load_dotenv

load_dotenv()

table_name = "wp_gf_entry_meta"

openai.api_key = os.getenv("OPENAI_API_KEY")

# Read MySQL credentials from environment variables using dotenv
mysql_host = os.getenv("MYSQL_HOST")
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_database = os.getenv("MYSQL_DATABASE")
mysql_port = os.getenv("MYSQL_PORT")
print("Port type:", type(mysql_port), "Port value:", mysql_port)
mysql_socket = os.getenv("MYSQL_SOCKET")

mysql = Mysql(mysql_host, mysql_user, mysql_password, mysql_database, int(mysql_port), mysql_socket)
table_schema = mysql.get_table_schema(table_name)
print("MySQL connection:", mysql)
model_engine = "davinci"

def execute_mysql_query(query_text, db_instance):
    print('Query text:', query_text)
    try:
        completions = openai.Completion.create(
            engine=model_engine,
prompt=f"Using the following database schema for table '{table_name}':\n{table_schema}\n\nTranslate the following natural language question into a SQL query:\n\"{query_text}\"\n\nSQL Query:",
            max_tokens=100,  # Reduce max_tokens to a smaller value
            n=1,
            stop=None,
            temperature=0.7  # Adjust temperature to control randomness
        )
        print('Completion text:', completions.choices[0].text)

        completion_text = completions.choices[0].text.strip()

        # Split the response by newline characters and take only the first line
        completion_text = completion_text.split('\n')[0]

        # Check if the completion_text is a valid SQL query
        if completion_text.startswith(("SELECT", "INSERT", "UPDATE", "DELETE")):
            try:
                print('Executing query:', completion_text)
                result = db_instance.execute(completion_text)
            except:
                print('I am sorry, there was an error executing the query.')
                return 'I am sorry, there was an error executing the query.'
            return str(result)
        else:
            print('I am sorry, I do not understand the query.')
            return 'I am sorry, I do not understand the query.'
    except:
        print('I am sorry, I did not understand your prompt.')
        return 'I am sorry, I did not understand your prompt.'

# Add this at the end of the mysql_flow.py script
if __name__ == "__main__":
    # Test query
    test_query = "SELECT * FROM wp_gf_entry_meta WHERE meta_value LIKE '%leather%' AND meta_key = 7"
    # Call the execute_mysql_query function with the test query
    result = execute_mysql_query(test_query, mysql)
    # Print the result
    print(result)
