This is a folder for what is planned to be a basic python web scraper script that pulls data from dynamic funds pages for current stocks within a portfolio (e.g. dynamic us etf) and puts them in a sqlite database along with the 'As at' date. 

The purpose is to routinely collect the stock holding over time in order to review each quarter which stocks were purchased and sold from the portfolio compared to last quarter. 

Idea being if a new stock is aquired, we can analyze it and see why dynamic is interested in this specific stock. 

The problem is, currently there is no way of knowing how long a specific stock has been in a portfolio. For example, trimble might be the top holding, but did they buy in years ago, or was this a recent purchase? This script will be able to track changes over time. 