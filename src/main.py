import queries as q
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


def get_graphql_client(endpoint: str = "https://public-api.defiyield.app/graphql/") -> Client:
    """
    Creates GraphQL client, if no endpoint is provided, the DeFiYield App endpoint is used
    :param endpoint: str
    :return: gql.Client
    """
    # Set transport with DefiYield url endpoint
    headers = {"X-Api-Key": "bad7014e-3fd4-473a-b981-1a5c2dd2d72e"}
    transport = AIOHTTPTransport(url=endpoint, headers=headers)

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client


if __name__ == "__main__":
    # Execute the query on the transport
    gql_client = get_graphql_client()

    chain_query = gql(q.query_get_chain_ids)
    chains = gql_client.execute(chain_query)
    print(chains)
