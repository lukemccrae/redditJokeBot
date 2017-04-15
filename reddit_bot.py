import praw
import time
import requests

def authenticate():
	print "Loggin in..."
	reddit = praw.Reddit('tellmeajokebot', user_agent = "tellmeajokebot")
	print "Authenticated as {}!".format(reddit.user.me())

	return reddit

def main():
	reddit = authenticate()
	joke = requests.get("http://api.yomomma.info/")
	while joke:
		run_bot(reddit, joke)

cache = []
askTheBot = ['tellmeajokebot']

def run_bot(reddit, joke):
	print "Obtaining 25 comments..."
	print joke
	subreddit = reddit.subreddit('test')
	comments = subreddit.comments(limit=25)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in askTheBot)
		if isMatch and comment.id not in cache:
			print 'replying to comment ' + comment.id
			comment.reply(joke)
			print "Replied to comment " + comment.id

	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...
	time.sleep(10)

#conditional to execute main function when script is imported
#avoids the code being invoked at the base level of the code
if __name__ == '__main__':
	main()
