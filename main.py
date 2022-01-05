import imghdr
import easyocr
import os
import sys
import filecmp
from datetime import datetime
from thefuzz import fuzz

def process_image(image, pattern, reader):
    try:
        result = reader.readtext(image, detail=0, paragraph=True)
        for line in result:
            similarity = fuzz.token_set_ratio(pattern.lower(), line.lower())
            if similarity >= 90:
                print(datetime.now(), 'INFO [process_image] Found pattern in the image', image, 'similarity', similarity, '%')
                break
    except:
        print(datetime.now(), 'ERROR [process_image] Cant process the image ', image)

def main():
    path, pattern, images = os.getenv('EABYKOV_PATH', '/tmp/'), os.getenv('EABYKOV_PATTERN', 'EABYKOV'), []
    if sys.version_info[0] < 3:
        sys.exit('ERROR [main] Need to use Python 3')
    else:
        print(datetime.now(), ' INFO [main] Python version is ', sys.version_info[0], '.', sys.version_info[1], '.', sys.version_info[2], sep="")
    if os.path.isdir(path) == False:
        sys.exit('ERROR [main] The path not exist or not a directory')
    else:
        print(datetime.now(), 'INFO [main] Will search pattern', pattern, 'in the directory', path)

    print(datetime.now(), 'INFO [list_images] Image list generation has started')
    for root, directories, files in os.walk(path):
        for name in files:
            if imghdr.what(os.path.join(root, name)):
                imageexist = False
                for image in images:
                    if filecmp.cmp(image, os.path.join(root, name)):
                        imageexist = True
                        break
                if imageexist == False:
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

    print(datetime.now(), 'INFO [main] End of processing by github.com/eabykov')

if __name__ == "__main__":
    main()
