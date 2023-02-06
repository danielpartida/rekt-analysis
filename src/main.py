import os
from typing import Tuple

import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

import queries as q


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


def get_all_rekts(client: Client, limit: int = 100) -> pd.DataFrame:
    """
    Fetches the top rekts by funds. If no limit is given, the first 100 are fetched
    :param limit: Upper limit to fetch for rekts
    :param client: GraphQL client
    :return: pandas DataFrame
    """
    page_size = 50
    number_of_loops = int(limit/page_size)
    list_rekts = []
    for i in range(1, number_of_loops+1):
        # Fetch data with GraphQL
        rekt_query = q.get_rekt_query(page_number=i, page_size=page_size)
        rekts_response = execute_gql_query(client=client, query=rekt_query)

        # Transform data to DataFrame
        df_rekts = pd.DataFrame(data=rekts_response['rekts'])
        df_rekts.set_index(df_rekts.id, inplace=True)
        df_rekts.drop(columns=['id'], inplace=True)
        df_rekts.date = pd.to_datetime(df_rekts.date)
        df_rekts.sort_values(by=['date'], inplace=True)

        # Append current DataFrame to list of all DataFrames
        list_rekts.append(df_rekts)

    # Concat list of DataFrames into single combined DataFrame
    all_rekts = pd.concat(list_rekts)
    all_rekts[['fundsLost', 'fundsReturned']] = all_rekts[['fundsLost', 'fundsReturned']].apply(pd.to_numeric)

    return all_rekts


def get_count_statistics(series_with_count: pd.Series) -> Tuple:
    """
    Calculates count statistics for a given series
    :param series_with_count: pd.Series to calculate count statistics
    :return: Tuple
    """
    main_count = series_with_count.idxmax()
    max_count_percentage = round(max(series_with_count) / series_with_count.sum(), 4)

    return main_count, max_count_percentage


def run_main(limit: int = 1000, show_plots: bool = False, save_plots: bool = False) -> Tuple:
    """
    Main execution method. It follows 4 steps.
    1. Creates a GraphQL query for the Rekt database of DeFiYield App
    2. It fetches the rekt data and process the data
    3. It computes key metrics
    4. It plots key insights, displays the plots and saves the plots if parameter save_plots is True
    :param limit: Limit of rekts to fetch
    :param save_plots: bool, default value is False
    :return: Tuple
    """
    # 1. Create GraphQL query to fetch rekts
    gql_client = get_graphql_client()

    chains_response = execute_gql_query(client=gql_client, query=q.query_get_chain_ids)
    chains_list = chains_response['chains']

    # 2. Fetch rekts data and transform the data to DataFrame
    df_rekts = get_all_rekts(client=gql_client, limit=limit)
    df_copy = df_rekts.set_index('date')

    # 3. Compute key statistics
    issue_type_count = df_rekts.groupby(['issueType']).size()
    category_count = df_rekts.groupby(['category']).size()
    year_count = df_copy.groupby(pd.Grouper(freq='Y')).size()

    # 4. Plot insights
    fig = px.scatter(df_rekts, x="date", y="fundsLost", size="fundsLost", color="issueType", hover_name="category",
                     marginal_x='box', log_y=True, title='Log-plot funds lost over time')

    if show_plots:
        fig.show()

    if save_plots:
        fig.write_html('log_plot_funds_lost_over_time_hist.png')

    return df_rekts, issue_type_count, category_count, year_count


if __name__ == "__main__":
    df, issue_count, category_count, month_count, year_count = run_main(limit=100, show_plots=True, save_plots=False)
    print(df)
