test_query = """
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

longer_query = """
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