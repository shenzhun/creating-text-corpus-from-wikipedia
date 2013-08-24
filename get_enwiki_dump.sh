wget -np -k -L http://dumps.wikimedia.org/enwiki/20130805/enwiki-20130805-pages-articles-multistream.xml.bz2
echo Download complete

echo Start decompress
bcat enwiki-20130805-pages-articles-multistream.xml.bz2
echo Decompress done

