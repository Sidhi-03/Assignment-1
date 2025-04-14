from typing import List, Optional
import strawberry
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Bank as BankModel
from models import Branch as BranchModel

@strawberry.type
class BankType:
    id: int
    name: str

@strawberry.type
class BranchType:
    ifsc: str
    branch: str
    address: Optional[str]
    city: Optional[str]
    district: Optional[str]
    state: Optional[str]
    bank: BankType

@strawberry.type
class BranchEdge:
    node: BranchType

@strawberry.type
class BranchConnection:
    edges: List[BranchEdge]

@strawberry.type
class Query:
    @strawberry.field
    def branches(self) -> BranchConnection:
        db = SessionLocal()
        try:
            branches = db.query(BranchModel).all()
            edges = [
                BranchEdge(
                    node=BranchType(
                        ifsc=branch.ifsc,
                        branch=branch.branch,
                        address=branch.address,
                        city=branch.city,
                        district=branch.district,
                        state=branch.state,
                        bank=BankType(
                            id=branch.bank.id,
                            name=branch.bank.name
                        )
                    )
                )
                for branch in branches
            ]
            return BranchConnection(edges=edges)
        finally:
            db.close()

    @strawberry.field
    def branch(self, ifsc: str) -> Optional[BranchType]:
        db = SessionLocal()
        try:
            branch = db.query(BranchModel).filter(BranchModel.ifsc == ifsc).first()
            if not branch:
                return None
            return BranchType(
                ifsc=branch.ifsc,
                branch=branch.branch,
                address=branch.address,
                city=branch.city,
                district=branch.district,
                state=branch.state,
                bank=BankType(
                    id=branch.bank.id,
                    name=branch.bank.name
                )
            )
        finally:
            db.close()

    @strawberry.field
    def banks(self) -> List[BankType]:
        db = SessionLocal()
        try:
            banks = db.query(BankModel).all()
            return [
                BankType(
                    id=bank.id,
                    name=bank.name
                )
                for bank in banks
            ]
        finally:
            db.close() 