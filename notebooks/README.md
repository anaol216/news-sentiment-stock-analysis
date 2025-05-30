# Notebooks Directory

This folder contains Jupyter notebooks for exploratory data analysis and initial data processing related to the financial news sentiment project.

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
  - Preparation steps for aligning stock data with news dates for correlation analysis  

## How to Use

Run these notebooks sequentially to understand the dataset from different angles:
1. Start with `eda_news.ipynb` for general data exploration.
2. Move to `sentiment_analysis.ipynb` to analyze news sentiment.
3. Use `stock_analysis.ipynb` to load stock data and prepare for further quantitative analysis.

---

Feel free to extend these notebooks with additional analysis, visualizations, or modeling as the project progresses.
