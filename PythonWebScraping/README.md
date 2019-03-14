# RugbyStats
A look into ESPN's available international rugby union scoring stats via StatsGuru

## Contents
* __countries.csv__: A list of countries, along with their international rugby tier, and abbreviations used if applicable.
* __preprocessed.csv__: The scraped data from `rugby_stats_final.csv` after processed through `PreProcessingScript.R` with new features
* __PreProcessingScript.R__: R script to do some general processing and addition of new features which may be useful for further analysis
* __rugby_stats_final.csv__: The output of web scraping from the ESPN StatsGuru database via `scraper.py`
* __scraper.py__: Simple web scraper using Python's `beautifulsoup`
* __README.md__: The document you are currently reading

## Supplemental Information
Rugby internationals Tier list:
https://en.wikipedia.org/wiki/List_of_international_rugby_union_teams

ESPN StatsGuru:
http://stats.espnscrum.com/statsguru/rugby/stats/index.html
