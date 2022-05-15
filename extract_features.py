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
imagePaths = ns.load_images_from_folder(args["dataset"])

# initialized the features matrix and labels
features = []
labels = []

# loop over the input images
for imagePath in imagePaths:
    # load the image from the dataset folder and extract the class
    # labels from the filename. Suppose the path is described as
    # ./dataset/{Class name}.{image number}.jpg
    image = cv2.imread(imagePath)
    imageID = ns.extract_filename(imagePath)

    # extract the colors in the histogram that explains the distribution of colors
    # within each pixels in all the images within the dataset
    histogram = ns.extract_color_histogram(image)
    histogram = histogram.tolist()

    # save the histogram along with the image name
    features.append(histogram)
    labels.append(imageID)

# open the output CSV file for writing
csv_writer = open(args["index"], "w")

for (imageID, image) in zip(labels, features):
    featureVector = ",".join([str(data) for data in image])
    csv_writer.write("{},{}\n".format(imageID, featureVector))

# close the CSV file
print("[INFO] saving features and model...")
csv_writer.close()
print("[INFO] Process completed...")
