# Find text on images

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/eabykov)

A small python script to find text on images. Uses [EasyOCR](https://github.com/JaidedAI/EasyOCR) and [thefuzz](https://github.com/seatgeek/thefuzz)

1. Install requirements by command `python3.8 -mpip install -r ./requirements.txt`
2. Set up global variables
- `PATTERN_TO_SEARCH` - text that we need to find
- `PATH_TO_DIR` - directory with images

3. Exec script `python3.8 ./easyocr.py`
