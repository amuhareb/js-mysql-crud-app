import MySQLdb

class MySQLInteraction:
    
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        
    def connect_to_database(self):
        self.connection = MySQLdb.connect(
            host=self.host, user=self.user, password=self.password, database=self.database
        )
        self.cursor = self.connection.cursor()
        
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        
    def create_table(self, table_name, column_data):
        
        create_table_query = "create table if not exists {} ({});".format(
            table_name, column_data
        )
        self.cursor.execute(create_table_query)
        
    def select_all_data_from_table(self, table_name):
        
        select_all_data_query = "select * from {};".format(table_name)
        self.cursor.execute(select_all_data_query)
        rows = self.cursor.fetchall()
        return rows
        
    def select_data_from_table(self, table_name, filter_data):
        
        select_data_query = "select * from {} where {};".format(table_name, filter_data)
        self.cursor.execute(select_data_query)
        rows = self.cursor.fetchall()
        return rows
        
    def update_table(self, table_name, update_data, filter_data):
        
        update_table_query = "update {} set {} where {};".format(table_name, update_data, filter_data)
        self.cursor.execute(update_table_query)
        self.connection.commit()
        
    def delete_data_from_table(self, table_name, filter_data):
        
        delete_data_query = "delete from {} where {};".format(table_name, filter_data)
        self.cursor.execute(delete_data_query)
        self.connection.commit()
