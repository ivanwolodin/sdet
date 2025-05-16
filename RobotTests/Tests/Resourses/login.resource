*** Settings ***
Library    Browser
Resource  ../Variables/login.robot

*** Keywords ***
Open Login Page
    New Browser    headless=false
    New Context
    New Page       ${LOGIN_URL}

Enter Username And Password
    [Arguments]    ${username}    ${password}
    Fill Text      input[type="text"]       ${username}
    Fill Text      input[type="password"]   ${password}
    Click          text=Login

Message Should Be
    [Arguments]    ${expected_text}    ${expected_color}
    Wait For Elements State    p    visible    timeout=5s
    Get Text    p    ==    ${expected_text}
    ${style}=    Get Attribute    p    style
    Should Contain    ${style}    ${expected_color}
