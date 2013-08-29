echo "Begin to download wiki dumps, pls wait..."
wget -np -k -L http://dumps.wikimedia.org/enwiki/20130805/enwiki-20130805-pages-articles-multistream.xml.bz2
echo "Download complete!"
sleep 2
echo "Start to decompress..."
bcat enwiki-20130805-pages-articles-multistream.xml.bz2
echo "Decompress done!"

split -b 200m enwiki-20130805-pages-articles-multistream.xml split-enwiki-part.
mkdir data
mv split-enwiki-part.* data/
