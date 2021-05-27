import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from routers.weather_router import weather_router

app = FastAPI()


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="WeatherClothes API",
        version="0.1.0",
        description="This is a OpenAPI schema WeatherClothes APPS",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": 'https://cdn.iconscout.com/icon/free/png-512/weather-192-461761.png'
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(weather_router)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000, debug=False)
