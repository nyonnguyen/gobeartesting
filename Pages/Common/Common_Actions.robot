*** Settings ***
Library           GoBearCore
Resource          ./Common_Variables.robot

*** Keywords ***
Insurance Should Be Visible
    wait until element is visible  ${INSURANCE}

Navigate To Insurance
    Select Element  ${INSURANCE}