# Notebooks Directory

This folder contains Jupyter notebooks for exploratory data analysis and initial data processing related to the financial news sentiment and stock price project.

## Contents

- **eda_news.ipynb**  
  Performs exploratory data analysis on financial news headlines, including:

  - Headline length distribution
  - Publisher activity and article counts
  - Publication frequency over time
  - Keyword and phrase extraction for topic insights

- **sentiment_analysis.ipynb**  
  Applies sentiment analysis techniques to financial news headlines to quantify the tone of articles. Includes:

  - Sentiment scoring with NLP tools (TextBlob, VADER, etc.)
  - Distribution of sentiment scores
  - Examples of highly positive and negative headlines

- **stock_analysis.ipynb**  
  Loads and visualizes stock price data, providing initial insights into price movements and trends. Also includes:
  - Basic price trend plots
  - Data cleaning notes, including handling inconsistent column names and trimming whitespace in stock CSV files
  - Preparing stock data for merging with news sentiment by aligning date formats and removing timezone info
  - Merge steps for combining stock prices with sentiment data for correlation analysis

## How to Use

Run these notebooks sequentially to understand the dataset from different angles:

1. Start with `eda_news.ipynb` for general data exploration.
2. Move to `sentiment_analysis.ipynb` to analyze news sentiment.
3. Use `stock_analysis.ipynb` to load, clean, and merge stock data with news sentiment for further quantitative analysis.

## Important Notes

- Some stock CSV files have inconsistent column formatting (extra spaces in headers). The notebooks handle these by trimming whitespace to ensure proper parsing.
- The stock price and sentiment datasets use different datetime formats; `stock_analysis.ipynb` removes timezone info from dates to enable successful merges.
- If you add new datasets, please verify column names and date formats to avoid merge errors.
