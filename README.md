# KABUKAYO

A sentiment analysis system that predicts U.S. stock market movements using NLP analysis of Reddit posts, designed to help retail traders make more informed investment decisions.

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Key Dependencies](#key-dependencies)
- [Workflow](#workflow)
- [Research Details](#research-details)
- [Results](#results)

## 🎯 Overview

This system uses Natural Language Processing (NLP) technology to analyze sentiment from posts on Reddit's stock-related subreddits and predict market movements. The project targets retail traders who may not have the same knowledge or information access as professional traders.

**Key Features:**
- Automated Reddit data collection from stock-related subreddits
- NLP-based sentiment analysis using VADER and RoBERTa models
- Trading strategy backtesting with configurable parameters
- Analysis of major stocks: Apple (AAPL), Amazon (AMZN), Meta (FB), Twitter (TWTR)

## 📁 Project Structure

```
kabukayo/
├── get-post-RAW.py                      # PRAW-based Reddit data collector (template)
├── get-posts.ipynb                      # Main data collection using PushShift API
├── data-split-clean.ipynb               # Text preprocessing and cleaning
├── vader-get.ipynb                      # Sentiment analysis with VADER model
├── backtest.ipynb                       # Trading strategy backtesting
├── reddit_data/                         # Raw Reddit posts datasets
│   ├── concat-aapl.csv                  # Apple-related posts
│   ├── concat-amzn.csv                  # Amazon-related posts
│   ├── concat-fb.csv                    # Meta-related posts
│   └── concat-twtr.csv                  # Twitter-related posts
└── train1118/                           # Training data and models
    ├── roberta-train1118.ipynb          # RoBERTa model training notebook
    └── training_aapl.csv                # Labeled training dataset
```

### File Descriptions

| File | Purpose |
|------|---------|
| **get-post-RAW.py** | Template script using PRAW (Python Reddit API Wrapper) for direct Reddit API access. Requires valid Reddit app credentials. |
| **get-posts.ipynb** | Data collection notebook using PushShift API to scrape Reddit posts from specified timeframes and keywords. |
| **data-split-clean.ipynb** | Data preprocessing pipeline: removes stopwords (preserving negations), applies lemmatization, handles contractions, filters duplicates. |
| **vader-get.ipynb** | Applies VADER (Valence Aware Dictionary and sEntiment Reasoner) model to analyze sentiment polarity of Reddit post titles. |
| **roberta-train1118.ipynb** | Trains RoBERTa (Robustly Optimized BERT) transformer model for binary sentiment classification with class imbalance handling. |
| **backtest.ipynb** | Evaluates trading strategy performance by merging stock price data with sentiment signals and comparing against buy-and-hold baseline. |

## 🚀 Installation

### Prerequisites
- Python 3.7+
- Jupyter Notebook or JupyterLab
- Reddit API credentials (for get-post-RAW.py)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/chinggisod/kabukayo.git
cd kabukayo
```

2. Install required packages:
```bash
pip install praw psaw pandas nltk contractions tensorflow scikit-learn imbalanced-learn seaborn matplotlib wordcloud
```

3. Download NLTK data:
```bash
python -m nltk.downloader stopwords wordnet omw-1.4
```

4. (Optional) For PRAW-based collection, configure Reddit API credentials in `get-post-RAW.py`:
```python
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)
```

## 📦 Key Dependencies

| Category | Libraries |
|----------|-----------|
| **Data Collection** | `praw`, `psaw` (PushShift API Wrapper) |
| **NLP & Text Processing** | `nltk`, `contractions`, `transformers` |
| **Machine Learning** | `tensorflow`, `scikit-learn`, `imbalanced-learn` |
| **Data Analysis** | `pandas`, `numpy` |
| **Visualization** | `matplotlib`, `seaborn`, `wordcloud` |

## 🔄 Workflow

Execute notebooks in the following order:

1. **Data Collection** (`get-posts.ipynb`)
   - Scrape Reddit posts from stock-related subreddits
   - Configure timeframes and target keywords
   - Output: Raw post data in `reddit_data/`

2. **Data Preprocessing** (`data-split-clean.ipynb`)
   - Clean and preprocess text data
   - Remove noise, apply lemmatization
   - Filter duplicates and low-quality posts

3. **Sentiment Analysis** (`vader-get.ipynb`)
   - Apply VADER model to generate sentiment scores
   - Create trading signals based on sentiment polarity
   - Output: Sentiment-labeled datasets

4. **Model Training** (Optional: `train1118/roberta-train1118.ipynb`)
   - Train deep learning RoBERTa model
   - Handle class imbalance with oversampling
   - Output: Trained sentiment classifier

5. **Backtesting** (`backtest.ipynb`)
   - Merge sentiment signals with stock price data
   - Simulate trading strategies with configurable lag parameters
   - Compare strategy returns vs. buy-and-hold benchmark
   - Output: Performance metrics and visualizations

## 🔬 Research Details

### 1. Background and Purpose

In recent years, there has been a growing interest in using natural language processing (NLP) technology to analyze the sentiment of posts on social networking services (SNS) and to predict market movements. In Japan, the number of retail traders (individuals who trade stocks without going through a brokerage firm) has been increasing rapidly against the backdrop of the economic recession. According to data from the Financial Services Agency, the number of individual investors in Japan reached a record 10.8 million in 2020, up nearly 50% from the previous year. Many of these people do not have the same knowledge or information access as professional traders. Therefore, we propose a system that predicts the movement of the U.S. stock market using NLP-based sentiment analysis from posts on the social networking platform called reddit. With the benefit of this tool, those who are new to retail trading can make more accessible investment decisions.

### 2. System Configuration

First, as shown in Figure 1, we collected a large amount of data on postings to various U.S. stock-related subreddits and their corresponding stock market data. This dataset consists of about 30,000 web-scraped posts from reddit, covering a period of about 10 months. We then apply NLP techniques to extract relevant features from the text and use the VADER model, a widely used tool for analyzing textual sentiment in social networking sites, as an NLP analyzer. Then, signals which indicate positive or negative tendencies generated by VADER are used to perform trading activities following a specific algorithm.

### 3. Simulation Results

In order to evaluate the performance of this system, a back-test analysis was conducted on the impact of various factors on the performance of the model, such as the choice of subreddits, trading day gap configurations, and specific stocks to be analyzed such as Apple, Amazon, Meta, and Twitter stocks. A number of results were achieved depending on these factors and the method of implementation strategy. The results showed that if the correct strategy is followed, our system is effective in generating profits larger than passive trading, as shown in Figure 2.

## 📊 Results

The backtesting analysis demonstrated that the sentiment-based trading strategy can outperform passive buy-and-hold strategies when properly configured. Performance varies based on:
- **Subreddit selection**: Different communities show varying signal quality
- **Trading day lag**: Optimal lag between sentiment signal and trade execution
- **Stock selection**: Performance differs across AAPL, AMZN, FB, and TWTR
- **Strategy implementation**: Trading rules and position sizing significantly impact returns

### 4. Summary

This system demonstrates the potential of using NLP sentiment analysis of reddit posts to provide more efficient and effective information about U.S. market trends to novice stock traders. In addition, by understanding what U.S. traders are discussing, the system can assist them in making effective investment decisions based on large amounts of information. In the future, we plan to expand this system to other SNSs and study various applications of sentiment analysis in the FX and crypto currency markets.

## ⚠️ Disclaimer

This project is for educational and research purposes only. Past performance does not guarantee future results. Always conduct your own research and consult with financial advisors before making investment decisions.

## 📄 License

This project is part of academic research. Please contact the repository owner for usage and licensing information.
