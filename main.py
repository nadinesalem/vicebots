# nadine salem
# main function to run the bot

import tweepy

api_key = 'RYnQs5J1ODk7ahJvKq3hloSBY'
api_key_secret = 'Ne66yZR2pYebfUBguV2yEomYmaUp2yqAuXy7UZCZpjYaV4Qxkc'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFwAiAEAAAAAGjIOja87Tu%2FhVdVPNobcUuPxqvI%3D2nIfC6ixnC9n3UHyB9DPCDzqctQJc7K3wE7bKnUgHKPmCj31mB'
key = '1579262271267774464-a3d4qQiiSpuGSVuNqiBv1WJ0KT27f5'
secret = '9ZNFReIGgKuOFCvjRJJCSvqjHEllGkORzdLdMdnAxrysn'

def api():
    auth = tweepy.OAuthHandler(api_key, api_keys_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)
    api.update_status('Hello World!')
