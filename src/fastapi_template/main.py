from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template v1.0.0",
    description="A pretty good template (I think)",
    responses={404: {"message": "Page not found"}},
)


@app.get("/")
def root():
    return {"message": "Root page :)"}
