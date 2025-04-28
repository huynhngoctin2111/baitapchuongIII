*** Settings ***
Documentation    Demo login test
Library          SeleniumLibrary

*** Variables ***
${URL}               https://the-internet.herokuapp.com/login
${USERNAME_VALID}    tomsmith 
${PASSWORD_VALID}    SuperSecretPassword!
${USERNAME_INVALID}  abc 
${PASSWORD_INVALID}  SuperSecretPassword!

*** Test Cases ***
Login Valid
    Mo Trinh Duyet
    Dang Nhap    ${USERNAME_VALID}    ${PASSWORD_VALID}
    Kiem Tra Dang Nhap Thanh Cong
    Dong Trinh Duyet

Login Invalid
    Mo Trinh Duyet
    Dang Nhap    ${USERNAME_INVALID}    ${PASSWORD_INVALID}
    Kiem Tra Dang Nhap That Bai
    Dong Trinh Duyet

*** Keywords ***
Mo Trinh Duyet
    Open Browser    ${URL}    chrome
    Maximize Browser Window

Dang Nhap
    [Arguments]    ${username}    ${password}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Element    xpath=//*[@id='login']/button

Kiem Tra Dang Nhap Thanh Cong
    Wait Until Element Is Visible    css:.flash.success    timeout=5s
    Element Should Contain           css:.flash.success    You logged into a secure area!

Kiem Tra Dang Nhap That Bai
    Wait Until Element Is Visible    css:.flash.error    timeout=5s
    Element Should Contain           css:.flash.error    Your username is invalid!

Dong Trinh Duyet
    Close Browser
