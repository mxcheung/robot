*** Settings ***
Library    ../libs/TimeHelper.py

*** Test Cases ***
Get Chicago Time From Python
    ${chicago}=    Get Chicago Time
    Log    Chicago time: ${chicago}
