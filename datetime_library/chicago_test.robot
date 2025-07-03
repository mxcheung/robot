*** Settings ***
Library    ../libs/TimeHelper.py

*** Test Cases ***
Get Time Using Timezone Keys
    ${chicago}=    Get Local Time    chicago
    ${ny}=         Get Local Time    new_york
    ${la}=         Get Local Time    los_angeles
    ${sydney}=     Get Local Time    sydney
    ${utc}=        Get Local Time    utc

    Log    Chicago time: ${chicago}
    Log    New York time: ${ny}
    Log    Los Angeles time: ${la}
    Log    Sydney time: ${sydney}
    Log    UTC time: ${utc}
