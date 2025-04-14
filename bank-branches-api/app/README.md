# Bank Branches API

A GraphQL API service for querying bank branch information.

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