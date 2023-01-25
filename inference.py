import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


def my_reco(user_id, country=None, books_type=None, n_reco=10, user_rating_threshold=20, n_similarity=10):
    """Import the model to predict the target"""
    a = f'hey {user_id}, {country}, {books_type}, {n_reco}, with {user_rating_threshold}, {n_similarity}'
    return [a]


@app.route('/my_user', methods=['GET'])
def my_user():
    """Perform the prediction using an API"""
    user_id = request.args.get('user_id')
    country = request.args.get('country')
    books_type = request.args.get('books_type')
    n_reco = request.args.get('n_reco')  # the number of recommandations
    user_rating_threshold = request.args.get('user_rating_threshold')  # drop users with not enough recommandations
    n_similarity = request.args.get('n_similarity')  # how many users we want to compare

    #input_data = np.array([user_id, country, books_type, n_reco, user_rating_threshold, n_similarity]).reshape(1, -1)
    # Perform the prediction using the inputs
    my_reco1 = my_reco(user_id, country, books_type, n_reco, user_rating_threshold, n_similarity)
    #my_reco2 = my_reco(user_id, country, books_type, n_reco, user_rating_threshold, n_similarity)
    #my_reco3 = my_reco(user_id, country, books_type, n_reco, user_rating_threshold, n_similarity)

    return my_reco1#, my_reco2, my_reco3


def main():
    """Group all the tasks in the right order"""
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
