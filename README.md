This project produces the non-anonymized version of the Gigaword summarization dataset, as used in the ACL 2017 paper [Get To The Point: Summarization with Pointer-Generator Networks](https://github.com/abisee/pointer-generator). It processes the dataset into the binary format expected by the code for the Tensorflow model.
## Run the script before running the main project
```
python mkdir.py
```
## Download Gigaword and process data
Download the data via the [URL](https://drive.google.com/open?id=1eNUzf015MhbjOZBpRQOfEqjdPwNz9iiS) and unzip it. Move the downloaded data to the empty directory **./data/datafiles**.
 ```
python ./data/data.py
```
## Convet the data into bin files format
```
python ./makedatafile/make_datafiles.py
```
