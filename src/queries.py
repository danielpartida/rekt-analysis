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