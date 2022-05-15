# import the necessary library
import os

# different type of image formats to consider
image_extensions = (".jpg", ".png", ".jpeg")

def is_upload_image(image_path):
    # check for only image file that was uploaded is on any of these
    # images types which included ".jpg", ".png", ".jpeg"

    image_path = image_path.lower()
    is_image_type = image_path.endswith(image_extensions)

    if is_image_type:
        return True
    else:
        return False

def load_images_from_folder(folder):
    # load all the images within a folder into memory
    image_list = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        image_list.append(path)

    return image_list


def extract_filename(path):
    # extract the filename from an absolute path
    return os.path.basename(path)

