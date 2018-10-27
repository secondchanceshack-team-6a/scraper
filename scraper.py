from bs4 import BeautifulSoup
import subprocess
import os
import db
from models.case import Case
from models.charge import Charge

FNULL = open(os.devnull, 'w')
list_of_href = []

data = subprocess.Popen(['./list.sh', 'montgomery', 'aa', "1"], stdout=subprocess.PIPE).stdout
soup = BeautifulSoup(data, 'html.parser')
table = soup.find("table", { "class" : "searchList" })

session = db.get_db_conn()

for row in table.findAll("tr")[1:]:
    tds = row.findAll("td")
    case = [tds[x].string for x in [2,3,4,5,6]]
    a = tds[1].find("a")
    case.insert(0, a.string)
    case = Case(name=case[0], case_number=case[1], case_name=case[2], status=case[3], filing_date=case[4], status_date=case[5])
    session.add(case)
    link = a['href'].split('=')[1]
    data = subprocess.Popen(['./ext.sh', 'montgomery', link], stdout=subprocess.PIPE, stderr=FNULL).stdout

    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", { "class" : "searchList" })
    tbody = table.find("tbody")
    tr = table.findAll("tr")[1]
    tds = tr.findAll("td")

    charge = [tds[x].string for x in [2,3,4,6,7]]
    print(case)
    print(charge)
    session.add(Charge(tca_code=charge[0], tca_desc=charge[1], filing_date=charge[2], violation_date=charge[3], disposition_date=charge[4], case_id=case.id))
