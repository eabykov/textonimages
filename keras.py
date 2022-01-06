import imghdr
import keras_ocr
import os
import sys
import filecmp
from datetime import datetime
from thefuzz import fuzz

def process_image(image, pattern, reader):
    try:
        for text, box in image:
            similarity = fuzz.token_set_ratio(pattern.lower(), text.lower())
            if similarity >= 90:
                print(datetime.now(), 'INFO [process_image] Found pattern in the image', image, 'similarity', similarity, '%')
                break
    except:
        print(datetime.now(), 'ERROR [process_image] Cant process the image ', image)

def main():
    path, pattern, images = os.getenv('EABYKOV_PATH', '/tmp/'), os.getenv('EABYKOV_PATTERN', 'EABYKOV'), []
    if sys.version_info[0] < 3 or os.path.isdir(path) == False:
        sys.exit('ERROR [main] Need to use Python 3.8 and path must be exist directory')
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
        keras_images = [keras_ocr.tools.read(image) for image in images]
        pipeline = keras_ocr.pipeline.Pipeline()
        prediction_groups = pipeline.recognize(keras_images)
    except:
        sys.exit('ERROR [easyocr_readers] Cant get Reader for RU and EN')

    for image in prediction_groups:
        process_image(image, pattern, reader)

    print(datetime.now(), 'INFO [main] End of processing by github.com/eabykov/textonimages')

if __name__ == "__main__":
    main()
