import os

import pandas as pd
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


def execute_gql_query(client: Client, query: str):
    """
    Executes GraphQL query given a client and query in form of str
    :param client: GraphQL client
    :param query: str
    :return: GraphQL response
    """
    chain_query = gql(query)
    gql_response = client.execute(chain_query)

    return gql_response


def get_all_rekts(client: Client):
    pass


if __name__ == "__main__":
    # Execute the query on the transport
    gql_client = get_graphql_client()

    chains_response = execute_gql_query(client=gql_client, query=q.query_get_chain_ids)
    chains_list = chains_response['chains']

    rekt_query = q.get_rekt_query(page_number=1, page_size=50)
    rekts_response = execute_gql_query(client=gql_client, query=rekt_query)
    df_rekts = pd.DataFrame(data=rekts_response['rekts'])
    df_rekts.set_index(df_rekts.id, inplace=True)
    df_rekts.drop(columns=['id'], inplace=True)
    df_rekts.date = pd.to_datetime(df_rekts.date)
    df_rekts.sort_values(by=['date'], inplace=True)
    print(df_rekts)