import requests

def get_categories():

    r = requests.get("https://api.escuelajs.co/api/v1/categories")  #Obtenemos información, se obtiene un estado
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json() 
    print(categories)                                          #Este formato lo transforma en una lista de diccionarios 
    
    cat = [item['name'] for item in categories]
    print(cat)