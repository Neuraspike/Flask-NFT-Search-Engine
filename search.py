# USAGE
# python search.py --query ./queries/bored_ape.png --index ./output/features.csv --dataset ./dataset
# python search.py --query ./queries/cryptopunk.png --index ./output/features.csv --dataset ./dataset
# python search.py --query ./queries/alien_frens.png --index ./output/features.csv --dataset ./dataset

# import the necessary libraries
import neuraspike as ns
import argparse
import cv2
import os

# setup the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--query", required=True, default="--query",
                help="path to the query image")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the featured will be stored")
ap.add_argument("-r", "--dataset", required=True, help="Path to the dataset folder")
args = vars(ap.parse_args())

# grab the image we want to search for convert from, BGR to LAB space
# then extract the color histogram which will be used to describe the
# query image and perform search among all the other dataset
print("[INFO] loading images...")
image = cv2.imread(args["query"])
query_image = ns.extract_color_histogram(image)

print("[INFO] Searching for similar images...")
result = ns.perform_image_search(query_image, args['index'], limit=10)

# display the query image
cv2.imshow("Query Image", image)

# iterate through the results
print("[INFO] Displaying similar images...")
for (image_id, score) in result:

    # load the image and display the output
    image_path = os.path.join(args['dataset'], image_id)
    query_result = cv2.imread(image_path)
    cv2.imshow("Result", query_result)
    cv2.waitKey(0)
