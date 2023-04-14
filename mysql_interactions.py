import openai_secret_manager
import openai
import mysql.connector
import os

MYSQL_USER = openai_secret_manager.get_secret('mysql_user')
MYSQL_PASSWORD = openai_secret_manager.get_secret('mysql_password')
MYSQL_HOST = openai_secret_manager.get_secret('mysql_host')
MYSQL_DATABASE = openai_secret_manager.get_secret('mysql_database')

openai.api_key = openai_secret_manager.get_secret('openai_key')['api_key']


def execute_query(query_str):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    cursor = conn.cursor()
    cursor.execute(query_str)
    result = cursor.fetchall()

    return result

def get_result(prompt):
    response = openai.Completion.create(
      prompt=prompt,
      engine="text-davinci-002",
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5
    )
    answer = response.choices[0].text.strip()
    return answer

if __name__ == '__main__':
    question = input("What's your question about MYSQL?")
    prompt = "mysql" + question
    result = get_result(prompt)
    print(result)

    while True:
        prompt = input('Do you have another question about MYSQL?')
        if not prompt.lower() in ['yes', 'y']:
            break
        question = input("What's your next question about MYSQL?")
        prompt = "mysql" + question
        result = get_result(prompt)
        print(result)
