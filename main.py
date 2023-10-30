from typing import Union
from fastapi import FastAPI
from conn import GetReposts
from fastapi.openapi.utils import get_openapi
from definitions import Report

tags_metadata = [
    {
        "name": "repots",
        "description": "Endpoint para retornar a ultima pontuação do rastreador.",
    },
]


app = FastAPI(
    
    openapi_url="/api/v1/openapi.json",
    swagger_ui_parameters={"syntaxHighlight": 'obsidian'})
reports = GetReposts()


@app.get("/repots")
def get_reports() -> list[Report]:
    teste = reports.returnDB()
    return teste

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API Reports",
        version="1.0.0",
        summary="API de reports",
        description="Api **OpenAPI** para poder ver todas as infromações do banco em relação ao rastreador.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
