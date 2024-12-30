from fastapi import FastAPI, HTTPException
import uvicorn
app = FastAPI()
if __name__ == '__main__':
    uvicorn.run('main:app')