import praw
import time

def authenticate():
	print "Loggin in..."
	reddit = praw.Reddit('dogbot', user_agent = "busterronitest's dog comment responder v0.1")
	print "Authenticated as {}!".format(reddit.user.me())

	return reddit

def main():
	reddit = authenticate()
	while True:
		run_bot(reddit)

def run_bot(reddit):
	print "Obtaining 25 comments..."
	for comment in reddit.subreddit('test').comments(limit=25):
		if "dog" in comment.body:
			print "String with \"dog\" found in comment " + comment.id
			comment.reply("I also love dogs! [Here](http://i.imgur.com/LLgRKeq.jpg) is an image of one!")
			print "Replied to comment " + comment.id

	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...
	time.sleep(10)

#conditional to execute main function when script is imported
#avoids the code being invoked at the base level of the code
if __name__ == '__main__':
	main()
