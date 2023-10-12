# BeautifulSoup 解析html表格

```shell
from bs4 import BeautifulSoup
import os
for root, dirs, files in os.walk("D:\\StanLong\\Python\\html_gxn"):
    for file in files:
        file_path = os.path.join(root, file)
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as fr:
            html_file = fr.read()
        soup = BeautifulSoup(html_file, 'html.parser')

        table = soup.findAll("table", id="vuln_list", class_="report_table")

        for node in table:
            trs = node.find_all('tr')
            for idx, tds in enumerate(trs):
                spans = tds.find_all('span', class_="level_danger_high")
                if len(spans) == 0:
                    continue
                for span in spans:
                    warn = str(span.string).strip()
                    print(warn)
                print(file_path)
```

