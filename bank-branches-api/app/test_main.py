import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, SessionLocal
from models import Bank, Branch
from main import app
import json

# Use SQLite in-memory database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    # Add test data
    db = TestingSessionLocal()
    try:
        # Create test bank
        bank = Bank(
            id=1,
            name="STATE BANK OF INDIA"
        )
        db.add(bank)
        db.commit()
        
        # Create test branch
        branch = Branch(
            ifsc="SBIN0000001",
            branch="HEAD OFFICE",
            address="MUMBAI",
            city="MUMBAI",
            district="GREATER MUMBAI",
            state="MAHARASHTRA",
            bank_id=bank.id
        )
        db.add(branch)
        db.commit()
        
        yield
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bank Branches API is running"}

def test_query_branches(client, test_db):
    # Test GraphQL query for branches
    query = """
    query {
        branches {
            edges {
                node {
                    ifsc
                    branch
                    address
                    city
                    district
                    state
                    bank {
                        name
                    }
                }
            }
        }
    }
    """
    
    response = client.post("/gql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "branches" in data["data"]
    assert "edges" in data["data"]["branches"]
    assert len(data["data"]["branches"]["edges"]) > 0
    assert "node" in data["data"]["branches"]["edges"][0]
    node = data["data"]["branches"]["edges"][0]["node"]
    assert node["ifsc"] == "SBIN0000001"
    assert node["branch"] == "HEAD OFFICE"
    assert node["address"] == "MUMBAI"
    assert node["city"] == "MUMBAI"
    assert node["district"] == "GREATER MUMBAI"
    assert node["state"] == "MAHARASHTRA"
    assert node["bank"]["name"] == "STATE BANK OF INDIA"

def test_query_banks(client, test_db):
    # Test GraphQL query for banks
    query = """
    query {
        banks {
            id
            name
        }
    }
    """
    
    response = client.post("/gql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "banks" in data["data"]
    assert len(data["data"]["banks"]) > 0
    assert data["data"]["banks"][0]["name"] == "STATE BANK OF INDIA" 