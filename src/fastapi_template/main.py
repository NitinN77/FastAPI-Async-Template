from fastapi import FastAPI

from fastapi_template.routers import main_router

app = FastAPI(
    title="FastAPI Template v1.0.1",
    description="A pretty good template (I think)",
    responses={404: {"message": "Page not found"}},
)

app.include_router(main_router)


@app.get("/")
def root():
    return {"message": "Root page :)"}
