# import the necessary library
import cv2

def extract_color_histogram(image, bins=(8, 8, 8)):
    # extract a 3D color histogram from the LAB color space using
    # the supplied number of `bins` per channel
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    histogram = cv2.calcHist([lab], [0, 1, 2], None, bins,
                             [0, 256, 0, 256, 0, 256])

    # normalizing the histogram
    cv2.normalize(histogram, histogram)

    # get the flattened histogram as the feature vector
    histogram = histogram.flatten()

    return histogram
