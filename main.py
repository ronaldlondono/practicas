from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def ruta_inicial():
    return {"Bienvenido": "bienvenido a mi api"}


@app.get('/prueba2')
def prueba2():
    return {"Bienvenido": "bienvenido a mi api"}
