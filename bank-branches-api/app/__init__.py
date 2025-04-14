from sqlalchemy import create_engine
from models import Base, Bank, Branch

engine = create_engine("sqlite:///./bank.db")
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

# Sample data
with Session() as session:
    # Clear existing data
    session.query(Branch).delete()
    session.query(Bank).delete()
    
    # Add banks
    banks = [
        Bank(id=1, name="State Bank of India"),
        Bank(id=2, name="HDFC Bank"),
        Bank(id=3, name="ICICI Bank")
    ]
    
    # Add branches
    branches = [
        Branch(
            ifsc="SBIN0000001",
            bank_id=1,
            branch="Mumbai Main Branch",
            address="Mumbai",
            city="Mumbai",
            district="Mumbai",
            state="Maharashtra"
        ),
        Branch(
            ifsc="HDFC0000001",
            bank_id=2,
            branch="Delhi Main Branch",
            address="Delhi",
            city="Delhi",
            district="Delhi",
            state="Delhi"
        )
    ]
    
    session.add_all(banks + branches)
    session.commit()
    print("Database initialized with sample data!")
