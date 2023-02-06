# rekt-analysis
Analysis of Rekt Database from DeFi Yield App

The Streamlit app can be found under this [link](https://intense-brook-89215.herokuapp.com/) Pending deployment!!! The application takes approx 30
seconds to pull the data from the DeFiYield App and render the key insights

This repository contains the analysis the major web3 rekts. The code is implemented under the src/ directory.
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

## Findings
### Note on number of rekts analyzed
I ran a rekt analysis with the 1000 rekts where the largest funds where lost. Some rekts are missing for this analysis.
However, I decided to focus just on the largest 1000 rekts to avoid exploiting the Rekt API. The user can fetch more rekts
by passing a larger limit to the get_all_rekts() method implemented under the main.py file. 

### Result images
**Saving images pending!!!**

Several images displaying findings and results are saved under the img/ folder

### Key insights
**Writing pending!!!**
- The more common rekt is...

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
  - Do analysis for token and chain -> in which chain and tokens do we find the biggest scams?
  - ~~What is the main category of exploits?~~
  - ~~What is the main type of exploit?~~
  - ~~Funds lost over time (year by year)?~~
  - ~~Ratio of lost and recovered funds~~
- Check with NLP details of exploit, for example keywords or topics
- ~~Deploy app to Heroku!!!~~

## Rekt endpoint
Paginated data about all hacks and exploits in [Rekt Database](https://docs.defiyield.app/audits/rekt-database).
Available fields:id, projectName,description, data, fundsLost, fundsReturned, chainIds, category, issueType, token 

## Future work
The following points are ideas on how to expand the current rekt analysis and continue the implementation
- Improve the performance of the Streamlit app. Another alternative is creating a Dash application where the render is
more performant
- Run seasonality analysis with [Prophet](https://facebook.github.io/prophet/docs/quick_start.html)
- Expand dashboard enabling further granular analysis on chain and token
- Analyze how a project token evolve after a scam. Analyze how costly is every scam for the ecosystem.
- Add text search for searching specific rekt in database