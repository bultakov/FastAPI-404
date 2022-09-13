from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


async def not_found(request, exc):
    return templates.TemplateResponse(
        name="404.html",
        context={
            'request': request
        },
        status_code=exc.status_code
    )


exceptions = {
    404: not_found,
}

app = FastAPI(title='Quiz App', debug=True, exception_handlers=exceptions)
app.mount("/static", StaticFiles(directory='static'), name="static")

templates = Jinja2Templates(directory='templates')


@app.get('/')
async def home():
    return {
        'message': "Assalomu Alaykum."
    }
