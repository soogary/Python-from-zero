"""this function uses the fire library to build  cli apps"""

import fire
from mylib.bot import mylib_scrape

if __name__ == "__main__":
    fire.Fire(mylib_scrape)
