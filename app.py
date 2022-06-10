import faulthandler
import filecmp
import imghdr
import os
import sys
from loguru import logger

import easyocr
from thefuzz import fuzz


def process_image(image, pattern, reader):
    try:
        logger.info(f"The search for pattern on the {image} has started")
        for line in set(reader.readtext(image, detail=0, paragraph=True)):
            similarity = fuzz.token_set_ratio(pattern.lower(), line.lower())
            if similarity >= 90:
                logger.info(
                    f"Found pattern in the image {image} similarity {similarity} %"
                )
                return image
                break
    except:
        logger.error(f"Cant search for the pattern on the image {image}")


def main():
    faulthandler.enable()
    path, pattern, images, outputImages = (
        os.getenv("PATH_TO_DIR", "/tmp/"),
        os.getenv("PATTERN_TO_SEARCH", "EABYKOV"),
        [],
        [],
    )
    logger.info(f"Will search pattern {pattern} in the directory {path}")

    for root, directories, files in os.walk(path):
        for name in files:
            imageexist = False
            for image in images:
                if filecmp.cmp(image, os.path.join(root, name)):
                    imageexist = True
                    break
            if imghdr.what(os.path.join(root, name)) and imageexist == False:
                images.append(os.path.join(root, name))
    if len(images) == 0:
        logger.error("Cant find images in the directory")
        sys.exit()
    else:
        logger.info(f"Found {len(images)} various images")
        images = set(images)

    try:
        logger.info("Trying to download the Reader for RU and EN")
        reader = easyocr.Reader(["ru", "en"])
        logger.info("Reader for RU and EN was downloaded")
    except:
        logger.error("Cant get Reader for RU and EN")
        sys.exit()

    outputImages = [
        image for image in images if process_image(image, pattern, reader) == image
    ]
    if len(outputImages) != 0:
        logger.error(f"Found pattern {pattern} on the images {outputImages}")


if __name__ == "__main__":
    main()
