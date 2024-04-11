import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("YOUR_CONSUMER_KEY", "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Define a function to handle new followers
def auto_respond_new_followers():
    for follower in tweepy.Cursor(api.followers).items():
        try:
            # Check if the follower is already followed or not
            if not follower.following:
                follower.follow()
                print(f"Started following {follower.screen_name}")

                # Send a direct message
                api.send_direct_message(follower.id, "Hey fam thanks for following! I'm trying to build the best community possible. It would mean the world if you could like my recent post and turn on notifications if you want. If you do, I will support back. Let's grow together! wgmi ❤️🚀")
                print(f"Sent a welcome message to {follower.screen_name}")
        except tweepy.TweepError as e:
            print(f"Failed to follow and send a message to {follower.screen_name}: {e}")

# Call the function to start auto-responding
auto_respond_new_followers()
