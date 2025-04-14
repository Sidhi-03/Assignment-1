# Bank Branches API

A GraphQL API service for querying bank branch information.

## Methodology

### Problem Analysis
1. Identified the need for a GraphQL API to query bank branch data
2. Analyzed the database schema with two main entities: Banks and Branches
3. Determined the need for a one-to-many relationship between Banks and Branches

### Solution Approach
1. **Database Design**
   - Created SQLAlchemy models for Banks and Branches
   - Established proper relationships and constraints
   - Used PostgreSQL for robust data storage

2. **API Development**
   - Implemented FastAPI for the web framework
   - Used Strawberry for GraphQL implementation
   - Created type-safe GraphQL schema
   - Implemented proper error handling

3. **Testing Strategy**
   - Set up Pytest framework
   - Created test fixtures for database
   - Implemented basic API tests

4. **Deployment Preparation**
   - Added Heroku deployment configuration
   - Set up environment variable management
   - Included database migration support

### Technical Decisions
1. **Framework Choice**: FastAPI + Strawberry
   - FastAPI for its modern async support and performance
   - Strawberry for type-safe GraphQL implementation

2. **Database Choice**: PostgreSQL
   - Robust relational database
   - Excellent support for complex queries
   - Reliable for production use

3. **Architecture**
   - Clean separation of concerns
   - Type-safe implementation
   - Scalable design

## Time Taken
- Problem Analysis: 30 minutes
- Database Design: 1 hour
- API Implementation: 2 hours
- Testing: 1 hour
- Documentation: 30 minutes
- Total Time: 5 hours

## Features

- GraphQL endpoint at `/gql`
- Query bank branches with associated bank information
- Clean code structure with proper separation of concerns
- Test cases for API functionality

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your database connection in `.env`:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

3. Run the application:
```bash
uvicorn main:app --reload
```

## Testing

Run the test suite:
```bash
pytest
```

## GraphQL Query Example

```graphql
query {
    branches {
        edges {
            node {
                branch
                bank {
                    name
                }
                ifsc
            }
        }
    }
}
```

## Deployment

The application can be deployed on Heroku:

1. Create a new Heroku app
2. Set up the PostgreSQL add-on
3. Configure environment variables
4. Deploy using Git

## License

MIT 
