import os
import requests
import pandas as pd
import zipfile

def check_download_unzip_read(filename, url, csv_filename):
	if os.path.exists(filename):
           	pass
	else:
    		req = requests.get(url)
    		assert req.status_code == 200 # if the download failed, this line will generate an error
    		with open(filename, 'wb') as f:
        		f.write(req.content)

	zf = zipfile.ZipFile(filename)
	data = pd.read_csv(zf.open(csv_filename))
	return data
