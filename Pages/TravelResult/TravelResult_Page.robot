*** Settings ***
Library           GoBearCore
Resource          TravelResult_Actions.robot

*** Keywords ***
User Should See Travel Result Page
    Travel Result Page Should Be Visible

User Set Min Slider Personal Accident On Filter
    [Arguments]  ${value}
    Set Min Slider Personal Accident  ${value}

User Set Max Slider Trip Cancellation
    [Arguments]  ${value}
    Set Max Slider Trip Cancellation  ${value}

User Expand The Filter Options
    Expand More Filter Options