# GraphQL
A GraphQL project for an agriculture management system. The system will handle data related to farms, crops, weather information, and equipment. It is more or less a practice project using Python with Flask for the backend, SQLAlchemy for database management, and Graphene for GraphQL integration.

## Running Flask App
Run the Flask app:
`python app.py`

Open `http://127.0.0.1:5000/graphql` to access the GraphiQL interface and test GraphQL API.

## Examples Queries
Example queries you can try:

To retrieve all farms:

`query {
  farms {
    id
    name
    location
    size
  }
}
`

To retrieve all crops:

`query {
  crops {
    id
    name
    type
    quantity
  }
}
`

To retrieve all weather information:

`query {
  weathers {
    id
    temperature
    humidity
    windSpeed: wind_speed
    farm {
      id
      name
      location
    }
  }
}
`

To retrieve all equipment:

`query {
  equipments {
    id
    name
    type
    farm {
      id
      name
      location
    }
  }
}
`