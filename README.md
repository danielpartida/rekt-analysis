# rekt-analysis
Analysis of Rekt Database from DeFi Yield App

## Sources
- [DeFiYield API docs](https://docs.defiyield.app/api/api#authentication)
- [Rekt Database docs](https://docs.defiyield.app/audits/rekt-database)
- [Rekt Database app](https://defiyield.app/rekt-database)

## Findings
### Note on number of rekts analyzed
I ran a rekt analysis with the 1000 rekts where the largest funds where lost. Some rekts are missing for this analysis.
However, I decided to focus just on the largest 1000 rekts to avoid exploiting the Rekt API. The user can fetch more rekts
by passing a larger limit to the get_all_rekts() method implemented under the main.py file. 

### Result images
Several images displaying findings and results are saved under the img/ folder

### Key insights
- The more common rekt is

## Instructions to run the script and replicate the results
- This code uses an API from DeFiYield App to fetch the rekt database. To maintain its privacy, the API key is stored 
under an .env file. Please add an .env file before executing the code and set your API value to the variable "X-Api-Key"
- To run the main.py script, install the dependencies in the requirements.txt file
- The queries should be made on the link https://public-api.defiyield.app/
- To test queries, use the DeFiYield [playground](https://public-api.defiyield.app/graphql/)

## Ideas to implement
- Start general
  - In which platform / chain do we find the biggest scams?
  - What is the main category of exploits? NFTs, Exchange, Metaverse, Token, Bridge?
  - What is the main type of exploit? Scam, exploit or hack?
  - Funds lost over time?
  - Ratio of lost and recovered funds
  - Which are the platforms that are the most secure & insecure?
  - How costly is every scam?
  - Distribution how often platforms are scammed
- Check with NLP details of exploit, for example keywords or topics
- Run with Prophet to analyze seasonality
- Create Dash or Streamlit application
- Visualize the rekt of the month
- How does the coin evolve after a scam?

## Rekt endpoint
Paginated data about all hacks and exploits in [Rekt Database](https://docs.defiyield.app/audits/rekt-database).
Available fields:id, projectName,description, data, fundsLost, fundsReturned, chainIds, category, issueType, token 

## Future work
- Do a Dash or Streamlit App that visualizes all results