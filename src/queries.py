query_get_chain_ids = """
query {
  chains {
    id
    absoluteChainId
    abbr
    name
    type
  }
}
"""

search_rekt_query = """
query {
  rekts(
    pageNumber:1
    pageSize:10
    searchText: "terra"
    orderBy: {
      fundsLost: desc
    }
  ){
    id
    projectName
    description
    fundsLost
  }
}
"""

# TODO: Make this query dynamic and change the pageSize to 50
description_query = """
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
  }
}
"""


def get_rekt_query(page_number: int = 1, page_size: int = 50) -> str:
    """
    Dynamically fetches rekts based on page_number and page_size. If no parameters are given, page_number starts at 1,
    and page_size is 50
    :param page_number: int
    :param page_size:  int
    :return: str rekt query
    """
    rekt_query = '''
    query {
      rekts(
        pageNumber: %s
        pageSize: %s
        orderBy: {
            fundsLost: desc
        }
      ) {
        id
        projectName
        description
        date
        fundsLost
        fundsReturned
        chaindIds
        category
        issueType
        token {
            name
        }
      }
    }
    ''' % (page_number, page_size)

    return rekt_query
