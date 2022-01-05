import imghdr
import easyocr
import os
import sys
import filecmp
from datetime import datetime
from thefuzz import fuzz

def process_image(image, pattern, reader):
    result = reader.readtext(image, detail=0, paragraph=True)
    for line in result:
        similarity = fuzz.token_set_ratio(pattern.lower(), line.lower())
        if similarity >= 90:
            print(datetime.now(), 'INFO  [process_image  ] Found pattern in the image', image, 'similarity', similarity, '%')
            break

def main():
    path, pattern, images = os.getenv('EABYKOV_PATH', '/tmp/'), os.getenv('EABYKOV_PATTERN', 'EABYKOV'), []
    if sys.version_info[0] < 3:
        print(datetime.now(), 'ERROR [main           ] Need to use Python 3')
        sys.exit()
    else:
        print(datetime.now(), ' INFO  [main           ] Python version is ', sys.version_info[0], '.', sys.version_info[1], '.', sys.version_info[2], sep="")
    if os.path.isdir(path) == False:
        print(datetime.now(), 'ERROR [main           ] The', path, 'not exist or not a directory')
        sys.exit()
    else:
        print(datetime.now(), 'INFO  [main           ] Will search pattern', pattern, 'in the directory', path)

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
        print(datetime.now(), 'ERROR [main           ] We cant find immages in the directory', path)
        sys.exit()
    else:
        print(datetime.now(), 'INFO  [get_list_images] Found', len(images), 'various images')

    reader = easyocr.Reader(["ru", "en"])
    for image in images:
        process_image(image, pattern, reader)

    print(datetime.now(), 'INFO  [main           ] End of processing by github.com/eabykov')

if __name__ == "__main__":
    main()
