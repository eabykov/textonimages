import os
import imghdr
from datetime import datetime
import easyocr
from thefuzz import fuzz

def process_image(image,pattern,reader):
    result = reader.readtext(image, detail=0, paragraph=True)
    for line in result:
        similarity = fuzz.token_set_ratio(pattern.lower(), line.lower())
        if similarity >= 90:
            print(datetime.now(), 'INFO [', process_image.__name__, '] Found pattern in the image', image, 'similarity', similarity, '%')
            break

def main():
    print(datetime.now(), 'INFO [', main.__name__, '] EABYKOV project 2022')
    path = os.getenv('EABYKOV_PATH', '/tmp/')
    print(datetime.now(), 'INFO [', main.__name__, '] Directory to check:', path)
    pattern = os.getenv('EABYKOV_PATTERN', 'EABYKOV')
    print(datetime.now(), 'INFO [', main.__name__, '] Will search pattern:', pattern)
    images = []

    for root, directories, files in os.walk(path):
        for name in files:
            if imghdr.what(root + '/' + name):
                images.append(os.path.join(root, name))

    reader = easyocr.Reader(["ru", "en"])
    print(datetime.now(), 'INFO [', main.__name__, '] Found images:', len(images))

    for image in images:
        process_image(image,pattern,reader)

    print(datetime.now(), 'INFO [', main.__name__, '] End of processing')

if __name__ == "__main__":
    main()
