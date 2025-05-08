from fastapi import FastAPI

app = FastAPI(
    title="ETL SaaS Platform",
    description="API-first ETL Platform to transfer data between databases",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the ETL SaaS Platform API"}
