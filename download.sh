mkdir datasets
cd datasets
wget "https://www.dropbox.com/s/0ybsudabqscstf7/biked_dataset.tar.gz" -q -O biked_dataset.tar.gz
tar -zxvf biked_dataset.tar.gz
rm biked_dataset.tar.gz

wget "https://www.dropbox.com/s/p6a615wd8qh6j7h/test_data.tar.gz" -q -O test_data.tar.gz
tar -zxvf test_data.tar.gz
rm test_data.tar.gz
