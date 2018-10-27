from bs4 import BeautifulSoup
import subprocess

result = subprocess.Popen(['./montgomery-list.sh', 'aa', '1'], stdout=subprocess.PIPE)
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

for link in list_of_href:
    result = subprocess.Popen(['./montgomery-ext.sh', link], stdout=subprocess.PIPE)
    data = result.stdout
    print(data.read())
