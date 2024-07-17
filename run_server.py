# Run uvicorn server

import uvicorn

if __name__ == "__main__":
    uvicorn.run("endpoint:app", port = 8000, reload = True,)
    
    