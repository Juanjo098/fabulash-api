# Fabulash api

Esta es una api de prueba para Fabulash creada con FasAPI y Uvicorn.

## Instalación

Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

### Clonar el repositorio

```bash
git clone https://github.com/Juanjo098/fabulash-api.git
```

### Instalar entorno virtual
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Instalar requerimientos
```bash
  pip install -r requirements.txt
```

### Levantar la api
```bash
uvicorn main:app --reload
```