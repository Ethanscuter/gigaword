This code produces the non-anonymized version of the Gigaword summarization dataset, as used in the ACL 2017 paper Get To The Point: Summarization with Pointer-Generator Networks. It processes the dataset into the binary format expected by the code for the Tensorflow model.
# Something must be done before running the code
  python mkdir.py
It will make some directories needed.
# Download data and process data
1. Download the data from the [url][1] https://drive.google.com/open?id=1eNUzf015MhbjOZBpRQOfEqjdPwNz9ii and unzip it. Replace the empty directory ./data/datafiles with the data you have downloaded.
2. python ./data/data.py
# Convet the data into bin files
python ./makedatafile/make_datafiles.py
[1]:  https://drive.google.com/open?id=1eNUzf015MhbjOZBpRQOfEqjdPwNz9ii
