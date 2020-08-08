
# image-downloader
A python script that takes arguments via the terminal to download images from a given URL, image category, and range. At the moment, the only format it downloads images in is jpg.
# Usage
 - Doing `python download_images.py -h` displays the help page that details what each required argument should be and what it is for.

**Examples**
 -   `python download_images.py https://acnhapi.com/v1/icons/fish/ fish 1 80`
 - `python download_images.py -url https://acnhapi.com/v1/icons/fish -img fish -start 1 -end 80`
