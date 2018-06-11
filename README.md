This code produces the non-anonymized version of the Gigaword summarization dataset, as used in the ACL 2017 paper [Get To The Point: Summarization with Pointer-Generator Networks](https://github.com/abisee/pointer-generator). It processes the dataset into the binary format expected by the code for the Tensorflow model.
## Something must be done before running the code
```
python mkdir.py
```
It will make some directories needed.
## Download data and process data
Download the data from the [URL](https://drive.google.com/open?id=1eNUzf015MhbjOZBpRQOfEqjdPwNz9iiS) and unzip it. Replace the empty directory ./data/datafiles with the data you have downloaded.
 ```
python ./data/data.py
```
## Convet the data into bin files
```
python ./makedatafile/make_datafiles.py
```
