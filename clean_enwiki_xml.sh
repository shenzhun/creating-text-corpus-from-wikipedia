#!/bin/env bash

split -b 200m enwiki-20130805-pages-articles-multistream.xml split-enwiki-part.
mv split-enwiki-part.* data/
cd data/
rm split-enwiki-part.aa.all.xmltext
python file2xmltext.py split-enwiki-part.aa.all
echo "Processing Done!"
sleep 2
cat split-enwiki-part.aa.all.xmltext | less
cd ..
