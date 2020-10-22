*** Settings ***

Library    selautomation.py
Test Setup  RunThisFirst
Test Teardown   RunThisLast

*** Test Cases ***
InvalidLogin
    login   ${INVALIDPASSWORD}   ${USERNAME}
    checkelement   #insert chosen xpath locator

Validlogin
    login   ${VALIDPASSWORD}   ${USERNAME}
    checkelement   #insert chosen xpath locator

InvalidsearchTest
    searchitem     ${BOOK1}
    sleep   3
    clickelem   #insert chosen xpath locator
    checkelement   #insert chosen xpath locator

ValidsearchTest
    searchitem     ${BOOK2}
    sleep   3
    scrolldown
    checkelement   #insert chosen xpath locator

Userisabletoscroll
    scrolldown
    checkelement   #insert chosen xpath locator
    sleep   3
    scrollup
    checkelement    #insert chosen xpath locator

*** Variables ***
${INVALIDPASSWORD}    #insert a random password
${USERNAME}     #insert username
${VALIDPASSWORD}    #insert password
${BOOK1}=   #insert item to be serched for invalid search test
${BOOK2}=   #insert item to be serched for valid search test

*** Keywords ***

RunThisFirst
   Run Keyword  selautomation.openbrowser

RunThisLast
   Run Keyword  selautomation.closebrowser

