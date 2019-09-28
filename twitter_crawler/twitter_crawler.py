#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Fan LEI'

#Using tweepy as a twitter API wrapper
import tweepy
from tweepy import OAuthHandler
import time
#Using panda to handle the dataframe
import pandas as pd

# twitterAPI authorisation
def twitterAPIAuth():
    # Oauth
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api = tweepy.API(auth)
    return api

def edgeGraphGenerater(users_list, friends_list):
    '''
    Generate edge graph and output the graph into a csv file
    :param users_list: Nodes in the graph each presents a twitter user
    :param friends_list: the friends of each twitter user in the users_list
    '''
    graph_list = []
    for i in range(len(users_list)):
        user = users_list[i]
        friends = friends_list[i]
        for friend in friends:
            edge = [user, friend]
            graph_list.append(edge)
    #print(graph_list)
    dump_data = pd.DataFrame(graph_list)
    dump_data.to_csv('edge_graph.csv', header=False, index=False)
    print('dump finished!')

def getUserInfo():
    '''
    Collect twitter users and their related friends.
    We choose Dr. Huanliu's twitter account as the start point to collect the friend graph.
    In this case in the project, we only collect all the friends of Dr. Huanliu and the first three Dr. Huanliu's friends' friend graphs on twitter.
    '''
    #setup twitter API object
    api = twitterAPIAuth()
    #We choose Dr. Huanliu's twitter account as the start point to collect the friend graph.
    user = api.get_user("liuhuan")
    user_id = user.id
    users_list = []
    friends_list = []
    temp = []

    #Collect Dr.Huanliu's twitter friends
    start_point = api.friends_ids('liuhuan')
    #follower_start = api.followers_ids('liuhuan')

    users_list.append(user_id)
    friends_list.append(start_point)
    print(len(start_point))

    #Collect friends of the first three friends of Dr. Huanliu
    for i in range(0,3):
        friend = start_point[i]
        try:
            new_friend_list = api.friends_ids(friend)
            friends_list.append(new_friend_list)
            users_list.append(friend)
            print("getting friend list of friend: %d " %(friend))
        except tweepy.RateLimitError:
            print('Reach 15 Minute Windows, 180 calls every 15 minutes.')
            time.sleep(15 * 60)
        except:
            print('may be network failing...try to reconnect...')
            try:
                new_friend_list = api.friends_ids(friend)
                friends_list.append(new_friend_list)
                users_list.append(friend)
                print("getting friend list of friend: %d again!!" % (friend))
            except:
                print("still cannot get the info, continue...")

    edgeGraphGenerater(users_list, friends_list)

#Collect all the friends of the friends of Dr.HuanLiu. (The second layer friends)
'''
    for friend in start_point:
        try:
            friends_list.append(api.friends_ids(friend))
            users_list.append(friend)
        except tweepy.RateLimitError:
            print('Reach 15 Minute Windows, 180 calls every 15 minutes.')
            time.sleep(15 * 60)
            try:
                friends_list.append(api.friends_ids(friend))
                users_list.append(friend)
            except:
                print("still cannot get the info, continue...")
        except:
            print('may be network failing...try to reconnect...')
            try:
                friends_list.append(api.friends_ids(friend))
                users_list.append(friend)
            except:
                print("still cannot get the info, continue...")
'''

# main method
if __name__ == "__main__":
    getUserInfo()