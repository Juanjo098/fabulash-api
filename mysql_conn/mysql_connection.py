from mysql import connector
# import random

class MySQLConnection():
  def __init__(self) -> None:
    self.__MYDB = connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="fabulash"
  )
  
  def query(self, table, fields='*', filters=''):
    response = []
    
    mycursor = self.__MYDB.cursor()

    # Ejemplo de consulta
    mycursor.execute(f"SELECT {fields} FROM {table} {filters}")
    
    column_names = [i[0] for i in mycursor.description]

    # Mostrar los resultados
    data = mycursor.fetchall()
    mycursor.close()
    
    for row in data:
      reg = []
      for info in zip(column_names, row):
        reg.append(info)
      response.append(dict(reg))
    
    return response
  
  def avance_query(self, query):
    response = []
    
    mycursor = self.__MYDB.cursor()

    # Ejemplo de consulta
    mycursor.execute(query)
    
    column_names = [i[0] for i in mycursor.description]

    # Mostrar los resultados
    data = mycursor.fetchall()
    mycursor.close()
    
    for row in data:
      reg = []
      for info in zip(column_names, row):
        reg.append(info)
      response.append(dict(reg))
    
    return response
  
  def close_connection(self):
    self.__MYDB.close()
  
  @property
  def connection_status(self):
    return self.__MYDB.get_server_info()
  
# conn = MySQLConnection()
# response = conn.query('servicio', fields='clvser, nombre, descripcion')
# for reg in response:
#  reg['stars'] = random.randint(1, 5)
# print(response)