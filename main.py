from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.get('/api/hello')
async def returnHello():
    return 'Hello, user'

@app.post('/api/greet')
async def returnGreeting(name: str):
    return (f'Hello, {name}')