import imghdr
import os
import sys
import filecmp
from datetime import datetime
import easyocr
import thefuzz

def process_image(image, pattern, reader):
    try:
        print(datetime.now(), 'INFO [process_image] The search for text on the', image, 'has started')
        for line in set(reader.readtext(image, detail=0, paragraph=True)):
            similarity = thefuzz.fuzz.token_set_ratio(pattern.lower(), line.lower())
            if similarity >= 90:
                print(datetime.now(), 'INFO [process_image] Found pattern in the image', image, 'similarity', similarity, '%')
                break
        print(datetime.now(), 'INFO [process_image] The search for the pattern in the', image, 'is finished')
    except:
        print(datetime.now(), 'ERROR [process_image] Cant search for the pattern on the image ', image)

def main():
    path, pattern, images = os.getenv('EABYKOV_PATH', '/tmp/'), os.getenv('EABYKOV_PATTERN', 'EABYKOV'), []
    if sys.version_info[0] < 3 or os.path.isdir(path) == False:
        sys.exit('ERROR [main] Please use Python 3 and path must be exist directory')
    else:
        print(datetime.now(), 'INFO [main] Python version', ".".join(map(str, sys.version_info[:3])))
        print(datetime.now(), 'INFO [main] EasyOCR version', easyocr.__version__)
        print(datetime.now(), 'INFO [main] TheFuzz', thefuzz.__version__)
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
        process_image(image, pattern, reader)
    print(datetime.now(), 'INFO [process_image] End of processing by github.com/eabykov/textonimages')

if __name__ == "__main__":
    main()
