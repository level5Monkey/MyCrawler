#!/bin/bash
while IFS= read -r keyword; do
    /bin/scrapy crawl AmazonCrawler -a keyword=$keyword 2>&1 | tee -a AmazonCrawler.log
    sleep $(( $RANDOM % 50 + 1))
done < /home/c0906/AmazonCrawler/keywords
