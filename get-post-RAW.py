import praw
import datetime

# Create a Reddit instance
reddit = praw.Reddit(client_id='your_client_id', client_secret='your_client_secret', user_agent='your_user_agent')

# Set the start and end dates for the data collection period
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2022, 12, 1)

# Set the subreddit to search
subreddit = reddit.subreddit('stocks')

# Search for posts containing the keyword "AAPL" within the specified date range
posts = subreddit.search('AAPL', sort='new', time_filter='year', limit=None)

# Iterate over the posts and print their titles
for post in posts:
    if post.created_utc >= start_date and post.created_utc <= end_date:
        print(post.title)
