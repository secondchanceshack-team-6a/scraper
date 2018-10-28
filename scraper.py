from bs4 import BeautifulSoup
import subprocess
import os
import db
from models.case import Case
from models.charge import Charge

FNULL = open(os.devnull, 'w')


# for county in [county.lowercase() for county in ["Bedford", "Cocke", "Giles", "Greene", "Hawkins", "Lawrence", "Macon", "Montgomery", "Obion", "Putnam", "Roane", "Robertson", "Rutherford", "Sullivan", "Sumner", "Washington", "Weakley", "Williamson"]]:
for i in range(1, 10):
    data = subprocess.Popen(['./list.sh', 'montgomery', "ad", str(i)], stdout=subprocess.PIPE).stdout
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", { "class" : "searchList" })

    session = db.get_db_conn()

    try:
        for row in table.findAll("tr")[1:]:
            tds = row.findAll("td")
            if tds[1] == "Defendant":
                break;
            case = [tds[x].string for x in [2,3,4,5,6]]
            a = tds[1].find("a")
            link = a['href'].split('=')[1]
            case.insert(0, a.string)
            case = Case(name=case[0], case_number=case[1], case_name=case[2], status=case[3], filing_date=case[4], status_date=case[5], url_id=link)
            session.add(case)
            session.commit()
            case = session.query(Case).filter_by(url_id=link).one()
            data = subprocess.Popen(['./ext.sh', 'montgomery', link], stdout=subprocess.PIPE, stderr=FNULL).stdout

            soup = BeautifulSoup(data, 'html.parser')
            table = soup.find("table", { "class" : "searchList" })
            tbody = table.find("tbody")
            tr = table.findAll("tr")[1]
            tds = tr.findAll("td")

            charge = [tds[x].string for x in [2,3,4,6,7]]
            session.add(Charge(tca_code=charge[0], tca_desc=charge[1], filing_date=charge[2], violation_date=charge[3], disposition_date=charge[4], case_id=case.id))
            session.commit()
    except:
        print("Error")

