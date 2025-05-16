*** Settings ***
Library           Browser
Resource          ../Resourses/login.resource
Suite Setup       Open Login Page
Suite Teardown    Close Browser

*** Test Cases ***
Login With Invalid Credentials
    Enter Username And Password    ${USERNAME}    ${INVALID_PASSWORD}
    Message Should Be    Ошибка при входе    red

Login With Valid Credentials
    Enter Username And Password    ${USERNAME}    ${VALID_PASSWORD}
    Message Should Be    Успешный вход    green
