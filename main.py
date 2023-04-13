from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.routers import authors, books
from database import Base, engine

tags_metadata = [
    {
        "name": "Author",
        "description": "Author Api's",
    },
    {
        "name": "Book",
        "description": "Book APi's"
    }
    ]
description = """
Author & Book API's
"""
app = FastAPI(
    openapi_tags=tags_metadata,
    title="Author&Book",
    description=description,
    version="0.0.1"
)
origins = [
    "http://localhost:4200",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authors.router)
app.include_router(books.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)

