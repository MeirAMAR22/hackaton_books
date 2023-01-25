import pandas as pd
import numpy as np
import requests


def my_client(val):
    """Request the API to predict the inputs"""
    keys = ['user_id', 'country', 'books_type', 'n_reco', 'user_rating_threshold', 'n_similarity']
    params = dict(zip(keys, val))
    response = requests.get('http://ec2-52-59-250-133.eu-central-1.compute.amazonaws.com:8080/my_user', params=params)
    response = str(response.json())
    print(response)
    return response


def main():
    """Group all the tasks in the right order"""
    my_client([1])


if __name__ == '__main__':
    main()
