#!/usr/bin/python

#reddit bot for scraping info from sale subreddits

import praw

def main():
    reddit = praw.Reddit("bot1", config_interpolation="basic")
    subreddit = reddit.subreddit("mechmarket")

    for submission in subreddit.stream.submissions(): #scan new submissions in subreddit
        scan_submissions(submission)

def scan_submissions(submission)
    cleaned_title = submission.title.lower() #sets title to lowercase for easier parsing
    if "[Vendor]" or "[Artisan]" or "[GB]" or "[IC]" or "[Service]" or "[Giveaway]" or "[Fundraiser]" in cleaned_title
        





if __name__ == "__main__":
    main()
