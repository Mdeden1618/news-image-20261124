[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Mdeden1618/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Mdeden1618/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

# Sum up 24 November's world news in one image

Entry for the [make.fun bounty "Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124).

- `main.py` (Python 3.13, no dependencies) copies the bundled `image.png`
  to `/output/entry.png`. No network, deterministic — both runs write
  identical bytes.
- `image.png`: 683x1024, 258 KB (limit: at most 1024x1024 px and 1 MiB).
  It holds JPEG data under the .png name, as the rules allow (a file is
  told apart by its first bytes). It sums up 24 November 2026 world news:
  Huawei found guilty of trade-secret theft and bank fraud (top left),
  Houthi drone attack on Riyadh's PIF Tower, 11 wounded (top right),
  tankers hit by mines in the Strait of Hormuz, Ukraine's drone strikes
  on Russian ships, the Cartagena supermarket siege, the Turkish
  helicopter crash killing 5, and Senegal regaining the Africa Cup of
  Nations title. The masthead names the day: 24 November 2026.
- `sources.txt`: 9 sources, all first reported on 24 November 2026, one
  per story.

Run: `python3 main.py` — writes `/output/entry.png`.
