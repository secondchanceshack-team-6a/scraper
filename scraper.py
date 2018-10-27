from bs4 import BeautifulSoup
import subprocess
import os
import db
import models.case
import models.charge

FNULL = open(os.devnull, 'w')
list_of_href = []
cases = []
charges = []

data = subprocess.Popen(['./montgomery-list.sh', 'aa', "1"], stdout=subprocess.PIPE).stdout
soup = BeautifulSoup(data, 'html.parser')
table = soup.find("table", { "class" : "searchList" })

session = db.get_db_conn()

for row in table.findAll("tr")[1:]:
    tds = row.findAll("td")
    case = [tds[x].string for x in [2,3,4,5,6]]
    for cell in tds:
        a = cell.find("a")
        if a != None:
            case.insert(0, a.string)
            cases.append(case)
            case_added = session.add(Case(name=case[0], case_number=case[1], case_name=case[2], status=case[3], filing_date=case[4], status_date=case[5]))
            for link in a['href'].split('=')[1]:
                data = subprocess.Popen(['./montgomery-ext.sh', link], stdout=subprocess.PIPE, stderr=FNULL).stdout

                soup = BeautifulSoup(data, 'html.parser')
                table = soup.find("table", { "class" : "searchList" })
                tbody = table.find("tbody")
                tr = table.findAll("tr")[1]
                tds = tr.findAll("td")

                charges.append([tds[x].string for x in [2,3,4,6,7]])
                session.add(Charge(tca_code=case[0], tca_desc=case[1], filing_date=case[2], violation_date=case[3], disposition_date=case[4], case_id=case_added.id))
