# import necessary packages
from flask import Flask, render_template, request, jsonify
from neuraspike import descriptor
from neuraspike import searcher
from neuraspike import config
from neuraspike import utils
from skimage import io
import os

# initialize the flask application
app = Flask(__name__)

# defined the path to the indexed feature, database of images, and query image
index_path = os.path.sep.join([config.BASE_STATIC_PATH, config.PATH_TO_INDEX])
image_path = os.path.sep.join([config.BASE_STATIC_PATH, config.PATH_TO_IMAGE])
upload_path = os.path.sep.join([config.BASE_STATIC_PATH, config.PATH_TO_UPLOAD_DIR])

INDEX = os.path.join(os.path.dirname(__file__), index_path)
print("[Info] web application is up and running")

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # initialize an empty list to store the results
        RESULT = []

        # request the path to the file
        image_url = request.files['query-image']

        # perform a quick check if an image was uploaded or not
        if image_url is None or image_url.filename == "":
            return jsonify({'error': 'Sorry, no file was uploaded'})

        # check if the image format uploaded is considered as a type
        # of image based on the uploaded format (.png, .jpg, .jpeg)
        if not utils.is_upload_image(image_url.filename):
            return jsonify({'error': 'Sorry, image format not supported'})

        try:
            # load the query image, reverse the input color-space from RGB into BGR
            # as the extract_color_histogram() function expects the input to be in BGR.
            # and then describe the image using color histograms
            query_image = io.imread(image_url)
            query_image = query_image[:, :, ::-1]
            features = descriptor.extract_color_histogram(query_image)

            # perform the search for similar images within among other features
            results = searcher.perform_image_search(features, INDEX)

            # loop over the results and append the correct path to the image folders
            for (image_id, score) in results:

                # update the path to the img of images
                image_id = os.path.sep.join([image_path, image_id])
                RESULT.append((round(score, 2), image_id))

            # defined the path to the uploaded image
            upload_image_path = os.path.sep.join([upload_path, image_url.filename])

            # return success by rendering the found similar images
            return render_template("index.html", query_image_path=upload_image_path,
                                   output=RESULT)

        except Exception as e:

            # return error
            return jsonify({"sorry": f"Sorry, no results! Please try again./"
                                     f"\nReason: {repr(e)}"}), 500

    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
