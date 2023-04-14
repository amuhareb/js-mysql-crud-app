from mysql_interactions import get_result, execute_query'\n\n# Insert data\nquery = \"INSERT INTO users (name, email) VALUES ('John', 'john@example.com')\"\nresult = get_result(query)\nprint(result)\n\n# Get data\nquery = \"SELECT * FROM users\"\nresult = execute_query(query)\nprint(result)\n