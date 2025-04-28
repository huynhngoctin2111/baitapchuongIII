*** Settings ***
Documentation    Đây là một script demo cho Robot Framework
Library          SeleniumLibrary

*** Variables ***
${x}    10
${y}    10

*** Test Cases ***
So Sanh Hai Bien
    Should Be Equal    ${x}    ${y}

Dieu Kien
    IF    ${x} == ${y}
        Log    ${x} = ${y}
    ELSE
        Log    ${x} != ${y}
    END

Test Case
    FOR    ${i}    IN RANGE    10
        Log To Console    ${i}
    END

Test Case 2
    TRY
        Click Element    id=btn-login
    EXCEPT
        Log To Console    Lỗi: không tìm thấy btn-login
    END