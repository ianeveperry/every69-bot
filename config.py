import tweepy
import logging
import yaml

# start logger
log_format = '%(asctime)s %(levelname)s: %(message)s'
log_date_format = '%Y-%m-%d %I:%M:%S %p'
logging.basicConfig(filename="log.txt", level="INFO",
                    format=log_format, datefmt=log_date_format)
logging.info("Bot activated")


def create_twitter_api():
    # read in api keys
    with open(r'api_keys.yaml') as file:
        keys = yaml.full_load(file)

    # parse the api keys
    app_key = keys['app twitter']['key']
    app_secret = keys['app twitter']['secret']
    posting_token = keys['niceaddresses twitter']['token']
    posting_secret = keys['niceaddresses twitter']['secret']

    # get the authentication token
    auth = tweepy.OAuthHandler(app_key, app_secret)
    auth.set_access_token(posting_token, posting_secret)

    # create the API
    api = tweepy.API(auth)

    # test that the API works
    try:
        api.verify_credentials()
    # if it doesn't log the error and throw the exception
    except Exception as e:
        logging.exception("Error creating API")
        raise e
    # if it works, log that it worked
    logging.debug("API created")

    # return the api object
    return(api)


def get_street_view_api_key():
    # read in api keys
    with open(r'api_keys.yaml') as file:
        keys = yaml.full_load(file)

    street_view_key = keys['google']['key']

    return(street_view_key)


def get_db_location():
    # read in api keys
    with open(r'api_keys.yaml') as file:
        keys = yaml.full_load(file)

    db_location = keys['database location']

    return(db_location)
