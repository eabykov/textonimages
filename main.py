import os
import imghdr
from datetime import datetime
import easyocr
from thefuzz import fuzz

def process_image(image,pattern,reader):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'INFO [', process_image.__name__, '] Process image:', image)
    result = reader.readtext(image, detail=0, paragraph=True)
    for line in result:
        if fuzz.token_set_ratio(pattern.lower(), line.lower()) >= 90:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'INFO [', process_image.__name__, '] Found the Text', pattern, 'in the file', image)
            break

def main():
    path = os.getenv('MDI_PATH', '/tmp/')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'INFO [', main.__name__, '] Directory to check:', path)
    pattern = os.getenv('MDI_PATTERN', 'MDI')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'INFO [', main.__name__, '] Will search pattern:', pattern)
    images = []

    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            root_name = root + '/' + name
            if imghdr.what(root_name):
                images.append(os.path.join(root, name))

    len_images = len(images)
    reader = easyocr.Reader(["ru", "en"])
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'INFO [', main.__name__, '] Found images:', len_images)

    for image in images:
        process_image(image,pattern,reader)

if __name__ == "__main__":
    main()
