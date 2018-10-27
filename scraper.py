from bs4 import BeautifulSoup
import subprocess
import os

i = 1
FNULL = open(os.devnull, 'w')
while True:
    result = subprocess.Popen(['./montgomery-list.sh', 'aa', str(i)], stdout=subprocess.PIPE)
    data = result.stdout

    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find("table", { "class" : "searchList" })

    list_of_href = []
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        for cell in cells:
            a = cell.find("a")
            if a != None:
                list_of_href.append(a['href'].split('=')[1])
            else:
                break;

    for link in list_of_href:
        result = subprocess.Popen(['./montgomery-ext.sh', link], stdout=subprocess.PIPE, stderr=FNULL)
        data = result.stdout
        print(data.read())
    i += 1
