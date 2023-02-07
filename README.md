# rekt-analysis
Analysis of Rekt Database from DeFi Yield App

The Streamlit app can be found under this [link](https://intense-brook-89215.herokuapp.com/). The application takes approx 
1min to pull the data from the DeFiYield App and render the key insights

This repository contains the analysis of the major web3 rekts. The code is implemented under the src/ directory.
Under the src/ directory, a Streamlit dashboard is implemented at src/app to visualize key insights. 
The data is fetched and processed at src/main.py. Inside the img/ directory, some plots are saved to visualize insights.
The repository has the following structure
```
project
│   README.md
│   requirements.txt
│   Procfile
│   setup.sh
│
└───img
│   │ figure_1.png  
│   │  ...
│   │ figure_n.png
└───src
    │   app.py
    │   main.py
    │   queries.py
```

## Sources
- [DeFiYield API docs](https://docs.defiyield.app/api/api)
- [Rekt Database docs](https://docs.defiyield.app/audits/rekt-database)
- [Rekt Database app](https://defiyield.app/rekt-database)

Available fields from Rekt database are: id, projectName,description, data, fundsLost, fundsReturned, chainIds, category, issueType, token

## Findings
### Note on number of rekts analyzed
I ran a rekt analysis with the 1000 rekts where the largest funds where lost. Some rekts are missing for this analysis.
However, I decided to focus just on the largest 1000 rekts to avoid exploiting the Rekt API. The user can fetch more rekts
by passing a larger limit to the get_all_rekts() method implemented under the main.py file. 

### Result images
Several images displaying findings and results are saved under the img/ folder

### Key insights
These are the insights that I gathered when fetching the 1000 largest rekts on the 7th of February 2023.
- The average lost of funds per rekt is approx. $74.7M. The average returned funds after occurred is approx. 5.95M
- Rekts have an increasing trend since 2011 with a peak on 2022
- The most frequent rekt issue are rugpulls, other issue types, and asset control. However, the most vulnerable issue 
type are undefined issues "other". A representative example under these undefined issue types is the collapse of the 
Terra Luna ecosystem where more than 40B dollars where wiped out. Abandoned issue types do not see funds returned durin
rekts. On the contrary, reentrancy have the largest returned funds with close to 66%
- The most frequent rekt categories are tokens, centralized finance (CeFi) and decentralized exchanges (DEX). However, 
the most vulnerable categories are stablecoins and borrowing/lending in CeFi. Borrowing and lending stablecoins from 
decentralized exchanges do not see funds returned during rekts. On the other hand, there are a high number of undefined
categories "other" that see 85% of the funds returned after a rekt

## Instructions to run the script and replicate the results
- This code uses an API from DeFiYield App to fetch the rekt database. To maintain its privacy, the API key is stored 
under an .env file. Please add an .env file before executing the code and set your API value to the variable "X-Api-Key"
- The working directory is the parent directory
- The queries are made on the link https://public-api.defiyield.app/
- To test other queries, use the DeFiYield [playground](https://public-api.defiyield.app/graphql/)
- To run the main.py script, install the dependencies in the requirements.txt file, then run src/main.py
- To run the Streamlit app, write in the command line "streamlit run src/app.py"

## Ideas to implement
- Start general
  - ~~Do analysis for category and for type of issue~~
  - ~~What is the main category of exploits?~~
  - ~~What is the main type of exploit?~~
  - ~~Funds lost over time (year by year)?~~
  - ~~Ratio of lost and recovered funds~~
  - Do analysis for token and chain -> in which chain and tokens do we find the biggest scams?
- Run NLP task to analyze details of exploit, for example keywords or topics
- ~~Deploy app to Heroku!!!~~

## Future work
The following points are ideas on how to expand the current rekt analysis and continue the implementation
- Improve the performance of the Streamlit app. Another alternative is creating a Dash application where the render is
more performant
- Run seasonality analysis with [Prophet](https://facebook.github.io/prophet/docs/quick_start.html)
- Expand dashboard enabling further granular analysis on chain and token
- Analyze how a project token evolve after a scam. Analyze how costly is every scam for the ecosystem.
- Add text search for searching specific rekt in database