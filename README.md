# Como usar

## Bibliotecas usadas
fastapi
Union
pyMongo

### Como instalar as Bibliotecas
```sh
  # insall fastapi
  pip3 install fastapi

  #install unicron
  pip3 install "uvicorn[standard]"

  #install pymongo
  pip3 install pyMongo


  #Rodar a api
  uvicorn main:app --reload
````
### Para acessar o Swagger e ver os Endpoints
```sh
  http://127.0.0.1:8000/docs
```