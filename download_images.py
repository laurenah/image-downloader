# imports
import urllib.request
import argparse

# parser
parser = argparse.ArgumentParser(description="Download multiple images from a URL into the folder where this file is located. For example: " +
                                            "using 'https://acnhapi.com/v1/icons/fish/' as the base URL, where every fish has an id from 1 to 80, " +
                                            "you would input the URL, maybe 'fish' as the image category, the starting id and the ending id. " +
                                            "This will save images named 'fish1.jpg', 'fish2.jpg' etc. into the folder where this file is executed")

# add arguments
parser.add_argument('-url', metavar='url', type=str, help='the base URL - should follow this format: https://site/image_category/')
parser.add_argument('-img', metavar='img', type=str, help='the main image name/category - for example: animal, or person. This assumes the site hosts an image for each item given the item id')
parser.add_argument('-start', metavar='start', type=int, help='the starting id of the images to download, must be a positive integer, and less than the end argument')
parser.add_argument('-end', metavar='end', type=int, help='the ending id of the images to download, must be a positive integer, and greater than the start argument')

# execute parse_args() method
args = parser.parse_args()
# collect args into variables
base_url = args.url
image_name = args.img
start = args.start
end = args.end

if (start <= 0 or start > end):
    print('start must not be negative or greater than end argument')
    exit()

if (end <= 0 or end < start):
    print('end must not be negative, or less than start argument')
    exit()

# for each id in the range supplied, fetch the image
for i in range(start, end+1):
    urllib.request.urlretrieve(base_url + str(i), image_name + str(i) + ".jpg")
    print("Downloaded " + image_name + str(i) + ".jpg")

print("-- Finished! --")