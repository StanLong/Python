# doc批量转docx

```python
import os
# pip install pypiwin32 -i https://pypi.douban.com
from win32com import client as wc
import time
word = wc.Dispatch("Word.Application")
for root, dirs, files in os.walk("D:\\StanLong\\project\\Idea\\doc"):
    for file in files:
        # print(os.path.join(root, file))
        file_path = os.path.join(root, file)
        # print(".".join(file_path.split(".")[:-1]))

        doc_name = word.Documents.Open(file_path)
        file_name = ".".join(file_path.split(".")[:-1])
        doc_name.SaveAs(file_name + ".docx", 12)
        time.sleep(1)
        doc_name.Close()
        print('done: ' + file)
word.Quit()
```

# 解析Html中的table

```python
import pandas as pd
from bs4 import BeautifulSoup
tables = pd.read_html("D:\\StanLong\\pythonProject\\html\\Test.html", header=0)
for rows in tables[0].values:
    print(rows[0], rows[1])
```

