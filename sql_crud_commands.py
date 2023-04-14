class Mysql:
    def select(self, columns: str = '*', table: str, where: str = None) -> list:
        with self.connection.cursor() as cursor:
            query = f'SELECT {columns} FROM {table}'
            if where:
                query += f' WHERE {where}'
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def insert(self, table: str, data: dict):
        with self.connection.cursor() as cursor:
            columns = ','.join(data.keys())
            values = [f'%({key})s' for key in data.keys()]
            query = f'INSERT INTO {table} ({columns}) VALUES ({','.join(values)})'
            cursor.execute(query, data)
            self.connection.commit()

    def delete(self, table: str, where: str) -> int:
        with self.connection.cursor() as cursor:
            query = f'DELETE FROM {table} WHERE {where}'
            cursor.execute(query)
            row_count = cursor.rowcount
            self.connection.commit()
            return row_count

    def update(self, table: str, data: dict, where: str) -> int:
        with self.connection.cursor() as cursor:
            set_clause = ', '.join([f'{key}=%({key})s' for key in data.keys()])
            query = f'UPDATE {table} SET {set_clause} WHERE {where}'
            cursor.execute(query, data)
            row_count = cursor.rowcount
            self.connection.commit()
            return row_count