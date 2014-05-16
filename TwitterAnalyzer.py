import twitter
import WOEIDRetriever

CONSUMER_KEY = 'Insert'
CONSUMER_SECRET = 'Here'
OAUTH_TOKEN = 'Your'
OAUTH_TOKEN_SECRET = 'Values'

def analyzeTrends(first_country, second_country):

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)

    country1 = first_country.get()
    country2 = second_country.get()

    country1_woeid = WOEIDRetriever.getWOEID(country1)
    country2_woeid = WOEIDRetriever.getWOEID(country2)

    country1_trends = twitter_api.trends.place(_id=country1_woeid)
    country2_trends = twitter_api.trends.place(_id=country2_woeid)

    country1_trends_set = set([trend['name'] for trend in country1_trends[0]['trends']])
    country2_trends_set = set([trend['name'] for trend in country2_trends[0]['trends']])

    common_trends = country1_trends_set.intersection(country2_trends_set)

    results = "Location 1: %s\n" %country1 + "Trends: %s\n\n" %country1_trends_set + "Location 2: %s\n" %country2 + "Trends: %s\n\n" %country2_trends_set + "Common Trends between %s and %s:\n" %(country1,country2) + "Trends: %s" %common_trends
    return results

