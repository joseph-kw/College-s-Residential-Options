import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()
#Getting Data from 1/5/2021 - 1/6/2021
before = int(dt.datetime(2021,6,1,0,0).timestamp()) 
after = int(dt.datetime(2021,5,1,0,0).timestamp())

subreddit="nus" #Retrieving comments
limit=100000
comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
print(f'Retrieved {len(comments)} comments from Pushshift')

comments_df = pd.DataFrame(comments) #Preview the comments data
comments_df.head(5)

comments_df.to_csv('./nus_comments.csv', header=True, index=False, columns=list(comments_df.axes[1]))

