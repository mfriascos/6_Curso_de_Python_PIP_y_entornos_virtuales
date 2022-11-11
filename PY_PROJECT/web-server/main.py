import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()                    #Se crea primer recurso

@app.get('/')                      #Decorador, se pone la ruta desde la cual por la web se va a ingresar 
def get_list():
    return [1,2,3,4]

@app.get('/contact')               #Esta es la ruta de contacto y se tiene una información diferente como un json 
def get_list():
    return {'name' : 'platzi'}

@app.get('/items', response_class = HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>HTML on Python!</title>
        </head>
        <body>
            <h1>Hello world, HTML on Python!</h1>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()