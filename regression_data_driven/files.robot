*** Settings ***
Library           OperatingSystem
Library           Collections

*** Variables ***
${DATA_DIR}       ./data

*** Test Cases ***
Log Each File In Folder As Separate Keyword
    ${files}=    List Files In Directory    ${DATA_DIR}
    FOR    ${file}    IN    @{files}
        Log File Content    ${file}
    END

*** Keywords ***
Log File Content
    [Arguments]    ${filename}
    ${file_path}=    Join Path    ${DATA_DIR}    ${filename}
    File Should Exist    ${file_path}
    ${content}=    Get File    ${file_path}
    Log    === ${filename} ===
    Log    ${content}
