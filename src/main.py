import os

import queries as q
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from dotenv import load_dotenv


def get_graphql_client(endpoint: str = "https://public-api.defiyield.app/graphql/") -> Client:
    """
    Creates GraphQL client, if no endpoint is provided, the DeFiYield App endpoint is used
    API keys are fetched from the .env file. To get a pair of API keys contact https://defiyield.app/
    :param endpoint: str
    :return: gql.Client
    """
    # Set transport with DeFiYield url endpoint
    load_dotenv()
    api_key = os.getenv("X-Api-Key")
    headers = {"X-Api-Key": api_key}
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
