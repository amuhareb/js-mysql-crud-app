import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

def select_data(table_name, column, value):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM {} WHERE {} = %s".format(table_name, column)
    mycursor.execute(sql, (value,))
    myresult = mycursor.fetchall()
    return myresult

print(select_data("customers", "name", "John Doe"))  # Sample data