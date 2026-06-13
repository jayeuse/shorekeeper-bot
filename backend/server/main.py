from fastapi import FastAPI
from server.core.migrations import upgrade_server_database

app = FastAPI()


@app.on_event("startup")
async def on_startup() -> None:
    upgrade_server_database()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.server.main:app", host="127.0.0.1", port=8001, reload=True)
