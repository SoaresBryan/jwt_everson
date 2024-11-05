from fastapi import FastAPI, HTTPException
import httpx
from db.connection import db 
from autenticator.auth_user import router as auth_router

app = FastAPI()

@app.get("/piada")
async def get_random_joke():
    url = "https://api.api-ninjas.com/v1/jokes"
    headers = {"X-Api-Key": "zT/1S8v/xhC6a/gKUWoYLQ==YEF5FHWLhzZHlBSX"} 

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()

        joke_data = response.json()
        joke_text = joke_data[0]["joke"]

        joke_entry = {"piada": joke_text}
        await db.piadas.insert_one(joke_entry)

        return {"piada": joke_text}

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Erro ao buscar piada")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno no servidor")

app.include_router(auth_router, prefix="/auth")