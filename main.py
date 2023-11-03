from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mysql_conn.mysql_connection import MySQLConnection

app = FastAPI()

# Configuración de CORS (Cross-Origin Resource Sharing) para permitir solicitudes de cualquier host en desarrollo
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/services')
async def servicies():
  conn = MySQLConnection()
  response = conn.query('servicio', fields='clvser, nombre, descripcion')
  conn.close_connection()
  return response

@app.get('/employees/{id}')
async def employess(id: int):
  """
    return [
    {
      'id': 1,
      'img': 'https://m.media-amazon.com/images/I/61kw0caY68L._AC_SX679_.jpg',
      'name': 'Jean Doe',
      'especialidad': 'Maquillista',
      'starsNumber': 4
    },
    {
      'id': 2,
      'img': 'https://media.licdn.com/dms/image/D4E22AQFbftSUOJcZyw/feedshare-shrink_2048_1536/0/1695837350432?e=1701907200&v=beta&t=pQ5HyS0t_-dnfFR0CooJAevpBw306PhMmfeUDzqrCyo',
      'name': 'Jean Doe',
      'especialidad': 'Maquillista',
      'starsNumber': 3
    },
    {
      'id': 3,
      'img': 'https://m.media-amazon.com/images/I/61v0moQ+INL._AC_SX679_.jpg',
      'name': 'Jean Doe',
      'especialidad': 'Maquillista',
      'starsNumber': 5
    },
    {
      'id': 4,
      'img': 'https://m.media-amazon.com/images/I/61v0moQ+INL._AC_SX679_.jpg',
      'name': 'Nueva empleada',
      'especialidad': 'Aprendiendo',
      'starsNumber': 2
    }
  ]
  """
  conn = MySQLConnection()
  response = conn.avance_query((
      f"select empleado.clvemp, empleado.nombre, empleado.apellido, empleado. descripcion, empleado.estrellas, empleado.imagen "
      f"from empleado "
      f"join ser_emp "
      f"on empleado.clvemp = ser_emp.clvemp "
      f"where ser_emp.clvser = {id};"
    )
  )
  conn.close_connection()
  return response

# print(conn.query('servicio', fields='nombre'))