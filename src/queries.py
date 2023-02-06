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


def get_rekt_query(page_number: int = 1, page_size: int = 50) -> str:
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
