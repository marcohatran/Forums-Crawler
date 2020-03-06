# Forums Crawler
A simple crawler for extracting all the topics and posts along with the user profile from the forum [Comodo](https://forums.comodo.com/).

**Topic URLS**
![Topic URL](/images/sub_topic.png)

**Posts URL**
![Posts links](/images/posts.png)

## Prerequisites

1. Python 3+
1. Pip
1. Scrapy module
    * You can download the scrapy module by using the command `pip install scrapy` or `pip3 install scrapy`

## How to run the code
1. Open the command prompt and go to the _tutorial_ directory.
1. Run the command `scrapy crawl forum -o forums.csv`
1. Then, run the command `scrapy crawl post -o posts.csv`

**Note**: The `-o` command is used to preserve the output in a file. The file formats supported by Scrapy are
* CSV
* JSON
* XML
* pickle
