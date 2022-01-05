import imghdr
import easyocr
import os
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
                images.append(os.path.join(root, name))

    reader = easyocr.Reader(["ru", "en"])
    print(datetime.now(), 'INFO [', main.__name__, '] Found images:', len(images))

    for image in images:
        process_image(image, pattern, reader)

    print(datetime.now(), 'INFO [', main.__name__, '] End of processing by github.com/eabykov 2022')

if __name__ == "__main__":
    main()
