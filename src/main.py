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
    gql_query = gql(query)
    gql_response = client.execute(gql_query)

    return gql_response


def get_all_rekt_summaries(client: Client, limit: int = 100) -> pd.Series:
    page_size = 50
    number_of_loops = int(limit / page_size)
    list_rekts = []
    for i in range(1, number_of_loops + 1):
        # Fetch data with GraphQL
        rekt_description_query = q.get_rekt_description_query(page_number=i, page_size=page_size)
        rekts_response = execute_gql_query(client=client, query=rekt_description_query)

        # Transform data to DataFrame
        df_rekt_descriptions = pd.DataFrame(data=rekts_response['rekts'])
        df_rekt_descriptions.set_index(df_rekt_descriptions.id, inplace=True)
        df_rekt_descriptions.drop(columns=['id'], inplace=True)

        # Append current DataFrame to list of all DataFrames
        list_rekts.append(df_rekt_descriptions)

    # Concat list of DataFrames into single combined DataFrame
    df_all_rekt_description = pd.concat(list_rekts)
    series_all_descriptions = df_all_rekt_description.description.dropna()

    # Process text and fetch only rekt summaries
    condition = '<p><strong>Quick Summary</strong></p><p>'
    filter = series_all_descriptions.apply(lambda x: '<p dir' not in x)
    descriptions_filtered = series_all_descriptions[filter]
    first_slice = descriptions_filtered.apply(lambda x: x.split(condition)[1] if condition in x else x.split('<p>')[1])
    summaries = first_slice.apply(lambda x: x.split('.&nbsp;</p>')[0])

    return summaries


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


def get_plots(df: pd.DataFrame) -> Tuple:
    fig_scatter_issue = px.scatter(
        df, x="date", y="fundsLost", size="fundsLost", color="issueType", hover_name="issueType", log_y=True,
        title='Interactive log-plot issue type funds lost over time'
    )

    fig_scatter_category = px.scatter(
        df, x="date", y="fundsLost", size="fundsLost", color="category", hover_name="category", log_y=True,
        title='Interactive log-plot category funds lost over time'
    )

    return fig_scatter_issue, fig_scatter_category


def run_main(limit: int = 1000, show_plots: bool = False) -> Tuple:
    """
    Main execution method. It follows 4 steps.
    1. Creates a GraphQL query for the Rekt database of DeFiYield App
    2. It fetches the rekt data and process the data
    3. It computes key metrics
    4. It plots key insights, displays the plots and saves the plots if parameter save_plots is True
    :param limit: Limit of rekts to fetch
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
    issue_type_mean = df_rekts.groupby(['issueType']).mean()
    category_count = df_rekts.groupby(['category']).size()
    category_mean = df_rekts.groupby(['category']).mean()
    year_count = df_copy.groupby(pd.Grouper(freq='Y')).size()

    # TODO: Do granular analysis with categories and issue type per year
    #  https://stackoverflow.com/questions/35898667/group-by-time-and-other-column-in-pandas
    # year_count_category = df_copy.groupby([pd.Grouper(freq='Y'), 'category']).size()
    # year_count_issue = df_copy.groupby([pd.Grouper(freq='Y'), 'issueType']).size()

    # 4. Plot insights
    fig_scatter_issue, fig_scatter_category = get_plots(df=df_rekts)

    if show_plots:
        fig_scatter_issue.show()
        fig_scatter_category.show()

    return df_rekts, issue_type_count, issue_type_mean, category_count, category_mean, year_count


if __name__ == "__main__":
    df, issue_count, issue_type_mean, category_count, category_mean, year_count = run_main(limit=100, show_plots=True)
