from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
from database import SessionLocal, engine, Base, get_db
from models import Bank, Branch
from schemas import BankType, BranchType, Query
from schema import schema

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Bank Branches API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create GraphQL router
graphql_app = GraphQLRouter(schema)

# Add GraphQL endpoint
app.include_router(graphql_app, prefix="/gql")

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Bank Branches API. Use /gql for GraphQL queries."} 