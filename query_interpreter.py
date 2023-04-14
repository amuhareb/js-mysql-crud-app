# Import mysql_flow module
import mysql_flow

# Helper function to extract keywords from GPT-3.5 completions

def extract_keywords(prompt):
    # List of non-CRUD keywords that should be ignored
    non_keywords = ['the', 'that', 'in', 'on', 'of', 'into', 'within']

    # split prompt string into words and remove non-CRUD fills/words
    words = prompt.split()
    keywords = [word for word in words if word.lower() not in non_keywords]

    # return the first two words as action + entity to perform
    if len(keywords) > 1:
        action, entity = keywords[:2]
        return action.lower(), entity.lower()
    else:
        return None, None

# Start the loop that will receive user queries and interpret them as CRUD operations
while True:
    prompt = input('Please enter your question: ')

    # check for 'exit' prompts to cleanly end program
    if prompt.lower() == 'exit':
        break

    # Derive CRUD operation and entity from prompt
    action, entity = extract_keywords(prompt)

    if action and entity:
        # Construct the query from the received prompt by appending a space to comply with python syntax
        query = f'{action.capitalize()} {entity} '
        print('Sending the following query to MYSQL:', query)
        # execute the query using the previously defined function
        mysql_flow.execute_query(query)
    else:
        print('I could not understand your question. Please refine it and try again. Please make sure you provide both an action word and an entity in your query.')
