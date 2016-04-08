import praw
import time



def run_bot():
    r = praw.Reddit(user_agent="/u/eddwinn")
    print('Logging in...')
    r.login('eddwinn', 'julie774')  # Promts for username and password if empty

    words_to_match = ['definately', 'definetely', 'definitly', 'definately']
    cache = []

    print('Grabbing subreddit...')
    subreddit = r.get_subreddit('onions').get_top(limit=100)  # Accesses r/test
    print('Grabbing comments...')

    for item in subreddit:
        print item.url

while True:
    run_bot()
    time.sleep(30)