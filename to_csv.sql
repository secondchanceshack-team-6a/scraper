.headers on
.mode csv
.output data.csv
SELECT ca.id as cases_id,
        ca.name as name,
        ca.case_number as case_number,
        ca.case_name as case_name,
        ca.status as status,
        ca.filing_date as filing_date,
        ca.status_date as status_date,
        ca.url_id as url_id,
        ch.id as charges_id,
        ch.tca_code as tca_code,
        ch.tca_desc as tca_desc,
        ch.filing_date as filing_date,
        ch.violation_date as violation_date,
        ch.disposition_date as disposition_date,
        ch.case_id as charge_case_id
FROM cases as ca
  INNER JOIN charges as ch
ON cases_id = charge_case_id;
