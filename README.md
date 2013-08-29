creating-text-corpus-from-wikipedia
===========================================

This project aims to create a plain text corpus from wikipedia for NLP and Speech Recognition.

Get Dumps
--------

Download the [20130805 dump](http://dumps.wikimedia.org/enwiki/20130805/) using [get_enwiki_dump.sh](https://github.com/shenzhun/creating-a-plain-text-corpus-from-wikipedia/blob/master/get_enwiki_dump.sh), the download and decompress process will last for a few hours due to its large size.(compress=10G, decompres=43G)

Extracte XML
------------
1. split enwiki dumps into 215 small files (200 MB/per file).

2. extracte text section into new file.

3. discard [wiki markup tags](http://en.wikipedia.org/wiki/Help:Cheatsheet) and extracte plain text into another new file.

4. write loop to process all the splited files into plain text files one by one.

