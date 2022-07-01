# USAGE
# python extract_features.py --dataset ./static/img/ --index ./static/output/features.csv

# import the necessary libraries
import neuraspike as ns
import argparse
import cv2

# setup the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to the dataset", type=str,
                default="./dataset")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the featured will be stored")
args = vars(ap.parse_args())

# grab the list of images that we'll be describing
print("[INFO] loading images...")
image_paths = ns.load_images_from_folder(args["dataset"])

# initialized the features matrix and labels
features = []
labels = []

# loop over the input images
for image_path in image_paths:
    # load the image from the dataset folder and extract the class
    # labels from the filename. Suppose the path is described as
    # ./dataset/{Class name}.{image number}.jpg
    image = cv2.imread(image_path)
    image_id = ns.extract_filename(image_path)

    # extract the colors in the histogram that explains the distribution
    # of colors within each pixel in all the images within the dataset
    histogram = ns.extract_color_histogram(image)
    histogram = histogram.tolist()

    # save the histogram along with the image name
    features.append(histogram)
    labels.append(image_id)

# open the output CSV file for writing
csv_writer = open(args["index"], "w")

# iterate through the labels & features then store the
# output in a CSV file
for (image_id, image) in zip(labels, features):
    feature = ",".join([str(data) for data in image])
    csv_writer.write("{},{}\n".format(image_id, feature))

# close the CSV file
print("[INFO] saving features and model...")
csv_writer.close()
print("[INFO] Process completed...")
