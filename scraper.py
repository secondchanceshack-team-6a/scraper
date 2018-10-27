from bs4 import BeautifulSoup
import subprocess
import os

FNULL = open(os.devnull, 'w')
list_of_href = []
cases = []
charges = []

data = subprocess.Popen(['./montgomery-list.sh', 'aa', "1"], stdout=subprocess.PIPE).stdout
soup = BeautifulSoup(data, 'html.parser')
table = soup.find("table", { "class" : "searchList" })

for row in table.findAll("tr")[1:]:
    tds = row.findAll("td")
    case = [tds[x].string for x in [2,3,4,5,6]]
    for cell in tds:
        a = cell.find("a")
        if a != None:
            list_of_href.append(a['href'].split('=')[1])
            case.insert(0, a.string)
            cases.append(case)

for link in list_of_href:
    data = subprocess.Popen(['./montgomery-ext.sh', link], stdout=subprocess.PIPE, stderr=FNULL).stdout

    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", { "class" : "searchList" })
    tbody = table.find("tbody")
    tr = table.findAll("tr")[1]
    tds = tr.findAll("td")

    charges.append([tds[x].string for x in [2,3,4,6,7]])

print(cases)
print(charges)
