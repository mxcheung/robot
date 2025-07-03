*** Settings ***
Library    ../libs/TimeHelper.py

*** Test Cases ***
Convert 6 And 8 Char UTC Date To Local Date
    ${local_date1}=    Convert UTC To Local Date    250703    chicago
    ${local_date2}=    Convert UTC To Local Date    20250703  new_york

    Log    Local date for '250703' (yyMMdd): ${local_date1}
    Log    Local date for '20250703' (yyyyMMdd): ${local_date2}
