# rekt-analysis
Analysis of Rekt Database from DeFi Yield App

## Sources
- [DeFiYield API docs](https://docs.defiyield.app/api/api#authentication)
- [Rekt Database docs](https://docs.defiyield.app/audits/rekt-database)
- [Rekt Database app](https://defiyield.app/rekt-database)

## Instructions
- pending
- The queries should be made on this link https://public-api.defiyield.app/
- Test your queries in the [playground](https://public-api.defiyield.app/graphql/)

## Ideas
- Start general
- In which platform / chain do we find the biggest scams?
- What is the main category of exploits? NFTs, Exchange, Metaverse, Token, Bridge?
- What is the main type of exploit? Scam, explot or hack?
- How does the coin evolve after a scam?
- Which are the platforms that are the most secure & insecure?
- Distribution how often platforms are scammed
- How costly is every scam?
- Ratio of lost and recovered funds
- Check with NLP details of exploit, for example keywords or topics

## Rekt endpoint
Paginated data about all hacks and exploits in [Rekt Database](https://docs.defiyield.app/audits/rekt-database).
Available fields:id, projectName,description, data, fundsLost, fundsReturned, chainIds, category, issueType, token 

## Future work
- Do a Dash or Streamlit App that visualizes all results