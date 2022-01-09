import os
import sys
import filecmp
import imghdr
import faulthandler
from datetime import datetime
from thefuzz import fuzz
import easyocr

def process_image(image, pattern, reader):
    try:
        print(datetime.now(), 'INFO [process_image] The search for pattern on the', image, 'has started')
        for line in set(reader.readtext(image, detail=0, paragraph=True)):
            similarity = fuzz.token_set_ratio(pattern.lower(), line.lower())
            if similarity >= 90:
                print(datetime.now(), 'INFO [process_image] Found pattern in the image', image, 'similarity', similarity, '%')
                return image
                break
    except:
        print(datetime.now(), 'ERROR [process_image] Cant search for the pattern on the image ', image)

def main():
    faulthandler.enable()
    path, pattern, images, outputImages = os.getenv('EABYKOV_PATH', '/tmp/'), os.getenv('EABYKOV_PATTERN', 'EABYKOV'), [], []
    if sys.version_info[0] < 3 or os.path.isdir(path) == False:
        sys.exit('ERROR [main] Please use Python 3 and path must be exist directory')
    else:
        print(datetime.now(), 'INFO [main] Python version', ".".join(map(str, sys.version_info[:3])))
        print(datetime.now(), 'INFO [main] EasyOCR version', easyocr.__version__)
        print(datetime.now(), 'INFO [main] Will search pattern', pattern, 'in the directory', path)

    print(datetime.now(), 'INFO [list_images] Image list generation has started')
    for root, directories, files in os.walk(path):
        for name in files:
            imageexist = False
            for image in images:
                if filecmp.cmp(image, os.path.join(root, name)):
                    imageexist = True
                    break
            if imghdr.what(os.path.join(root, name)) and imageexist == False:
                images.append(os.path.join(root, name))
    if images == []:
        sys.exit('ERROR [list_images] Cant find images in the directory')
    else:
        print(datetime.now(), 'INFO [list_images] Found', len(images), 'various images')

    try:
        print(datetime.now(), 'INFO [easyocr_readers] Trying to download the Reader for RU and EN')
        reader = easyocr.Reader(["ru", "en"])
        print(datetime.now(), 'INFO [easyocr_readers] Reader for RU and EN was downloaded')
    except:
        sys.exit('ERROR [easyocr_readers] Cant get Reader for RU and EN')

    for image in images:
        if process_image(image, pattern, reader) == image:
            outputImages.append(image)
    if outputImages == []:
        sys.exit('ERROR [main] Cant find pattern on the images')
    else:
        print(datetime.now(), 'INFO [main] Found pattern', pattern, 'on the images', outputImages)

if __name__ == "__main__":
    main()
