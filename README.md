# Find text on images

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/eabykov)

A small python script to find text on images. Uses [EasyOCR](https://github.com/JaidedAI/EasyOCR) and [thefuzz](https://github.com/seatgeek/thefuzz)

1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose V2](https://docs.docker.com/compose/cli-command/#installing-compose-v2)
2. Create `docker-compose.yml` file

```
services:
  textonimages:
    image: ghcr.io/eabykov/textonimages:v1.0.1
    environment:
      PATTERN_TO_SEARCH: ""
    volumes:
      - /local/folder/with/images:/tmp
```

> `PATTERN_TO_SEARCH` - text that we need to find

3. Run command `docker compose up -d`
4. Information about the matches found will be in the log `docker compose logs -f`

[![Stargazers over time](https://starchart.cc/eabykov/textonimages.svg)](https://starchart.cc/eabykov/textonimages)
