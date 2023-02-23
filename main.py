from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level='info', reload=True)


"""
Token Erick: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2Nzc3ODQxMjcsImlhdCI6MTY3NzE3OTMyNywic3ViIjoiMSJ9.g7tK2IqRRESjR5fk6RZ4HB9EWnFLCCjSyMaXVh1TlYY
Toekn Gisele: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2Nzc3ODU4NDYsImlhdCI6MTY3NzE4MTA0Niwic3ViIjoiMiJ9.BOMBIFGmYTkvY5NNkitecZl8xRQBCWs-2yA7HQc4G-E
Tipo: bearer
"""