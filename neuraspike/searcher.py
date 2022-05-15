# import the necessary libraries
from scipy.spatial import distance as dist
import numpy as np


def perform_image_search(query_feature, file_path, limit=10):
    # initialize the query result dictionary where the outputs
    # will be stored
    query_results = {}

    # loop over the rows in the data split file
    for row in open(file_path, 'r'):
        # extract the class label and features from the row
        row = row.strip().split(",")
        filename = row[0]  # get the filename
        features = np.array(row[1:], dtype="float32")  # get the features

        distance = euclidean_distance(query_feature, features)
        query_results[filename] = distance

    # sort the output based on the most relevant images at the first
    # of the list (i.e from the smallest to the largest distance) then
    # limit the result which will be returned
    query_results = sorted(query_results.items(), key=lambda value: value[1])
    query_results = query_results[:limit]

    return query_results


def euclidean_distance(query_image, image):
    return dist.euclidean(query_image, image)
