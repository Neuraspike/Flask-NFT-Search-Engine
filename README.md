## NFT Search Engine with Python and Flask

# NFT-Search-Engine


In this tutorial, we’ll learn how to transform our command-line based NFT Search Engine from the previous tutorial and turn it into a full-blown web application using Python and Flask.

## Dataset

For this tutorial, we will be utilizing a dataset that I manually scraped from the OpenSeas website (a market place where you could purchase NFTs) by downloading a bunch of NFTs profile picture projects.

The downloaded ones are:

    1) Bored Apes
    2) Cryptopunk, and
    3) Alien Frens


## Install

### &nbsp;&nbsp;&nbsp; Supported Python version
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python version used in this project: 3.8

### &nbsp;&nbsp;&nbsp; Libraries used

> * scipy~=1.7.1
> * numpy==1.17.4
> * opencv-contrib-python
> * Pillow
> * Flask
> * scikit-image

Otherwise, use the following command to install the packages according to the configuration file requirements.txt.

> *  pip install -r requirements.txt


## Code Walk-through 

For a more detailed explanation of the code, visit either of the following links:

> * Blog post: <a href="https://neuraspike.com/blog/adding-web-interface-nft-search-engine-flask/">here</a> 
> * Youtube:  <a href="https://www.youtube.com/watch?v=jWdHs6avKNs">here</a> 


## License

MIT License

Copyright (c) 2022 Neuraspike

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


 
#### USAGE
- git clone https://github.com/Neuraspike/Flask-NFT-Search-Engine

- cd Flask-NFT-Search-Engine

Before running the script, make sure you have all the requirements already installed.
 
- pip install -r requirements.txt

Now you can:

 - Extract features from the database of images: **python extract_features.py --dataset ./static/img/ --index ./static/output/features.csv**
 - Perform the search via localhost:5000: **python app.py**
 - Select an image from the folder directory: static/upload/
