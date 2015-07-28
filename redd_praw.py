import praw

user_agent = "L2T to Spotify:v0.1 by /u/drowning_porpoise"

r = praw.Reddit(user_agent=user_agent)
item_limit = 25
subredditName = "listentothis"

subreddit = r.get_subreddit(subredditName)
data = subreddit.get_top_from_week(limit=item_limit)
top_posts = {}

for thing in data:
    top_posts[post] = top_posts.get(post, 0) + thing.score

import pprint
pprint.pprint(top_posts)
