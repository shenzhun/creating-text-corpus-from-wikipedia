#!/bin/env bash

split -b 200m enwiki-20130805-pages-articles-multistream.xml split-enwiki-part.
find . -name split-enwiki-part.* > num_tmp
python xml2files.py
