from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
query_endpoint = "https://public-api.defiyield.app/graphql/"
headers = {"X-Api-Key": "bad7014e-3fd4-473a-b981-1a5c2dd2d72e"}
transport = AIOHTTPTransport(url=query_endpoint, headers=headers)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """
    query {
      rekts(
        pageNumber:1
        pageSize:10
        orderBy: {
          fundsLost: desc
        }
      ) {
        id
        projectName
        description
        fundsLost
        fundsReturned
        category
        token {
          name
        }
      }
    }
    """
)

if __name__ == "__main__":
    # Execute the query on the transport
    result = client.execute(query)
    print(result)
