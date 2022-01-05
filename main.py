import imghdr
import easyocr
import os
import filecmp
from datetime import datetime
from thefuzz import fuzz

def process_image(image, pattern, reader):
    result = reader.readtext(image, detail=0, paragraph=True)
    for line in result:
        similarity = fuzz.token_set_ratio(pattern.lower(), line.lower())
        if similarity >= 90:
            print(datetime.now(), 'INFO [', process_image.__name__, '] Found pattern in the image', image, 'similarity', similarity, '%')
            break

def main():
    path, pattern, images = os.getenv('EABYKOV_PATH', '/tmp/'), os.getenv('EABYKOV_PATTERN', 'EABYKOV'), []
    print(datetime.now(), 'INFO [', main.__name__, '] Will search pattern', pattern, 'in the directory', path)

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
    print(datetime.now(), 'INFO [', main.__name__, '] Found', len(images), 'various images')

    reader = easyocr.Reader(["ru", "en"])
    for image in images:
        process_image(image, pattern, reader)

    print(datetime.now(), 'INFO [', main.__name__, '] End of processing by github.com/eabykov')

if __name__ == "__main__":
    main()
