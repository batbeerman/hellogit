#Q1

#An access token is an object that describes the security context of a process or thread.
#The information in a token includes the identity and privileges of the user account associated with the process or thread.
#Access token for app.twitter.com
#	1008945469085618176-EcmSqixOPGZsE55LzWRpD174NWsNHK



#Q2
'''
  > nslookup www.google.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    www.google.com
Addresses:  2404:6800:4003:c03::68
          74.125.24.99
          74.125.24.106
          74.125.24.147
          74.125.24.105
          74.125.24.103
          74.125.24.104   

 > nslookup www.fb.com
    
Name:    star-z-mini.c10r.facebook.com
Addresses:  2a03:2880:f12f:87:face:b00c:0:50fb
          157.240.16.39
Aliases:  www.fb.co
'''

#Q3
import tweepy
consumer_key= "dIK9JxXXrhJBc7zhGLsM5xevW"
consumer_secret= "WqMctxuLR1XcEKu2clKsUjUA8lyNPEwHbQQNVdlcF0gVn080TK"
access_token= "	1008945469085618176-EcmSqixOPGZsE55LzWRpD174NWsNHK"
access_token_secret= "	j6G9xePAnixWqXZSDllIkrginmqgrAH2ALVjHOQ1F5aJy"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
status="testing"
api.update_status(status=status)


#Q4
'''
API is a part of library which defnes how an application communicates with external code.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required
for the use case.
For example, flickrj is an api client of Flickr for Java
And math is a library in Java.
'''


#Q5
import spotipy
the_local_train_uri = 'spotify:artist:7b6Ui7JVaBDEfZB9k6nHL0'
spotify = spotipy.Spotify()
results = spotify.artist_albums(the_local_train_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print((album['name']))
