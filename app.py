from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return """
    <html>
        <body>
            <h1>My X API App</h1>
            <p>This is a simple web app for X API authentication.</p>
        </body>
    </html>
    """

@app.get("/callback", response_class=HTMLResponse)
async def callback(request: Request):
    return """
    <html>
        <body>
            <h1>Authentication Successful</h1>
            <p>You can now close this window and use your CrewAI application.</p>
        </body>
    </html>
    """