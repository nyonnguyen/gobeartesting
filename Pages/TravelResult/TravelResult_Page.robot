*** Settings ***
Library           GoBearCore
Resource          TravelResult_Actions.robot

*** Keywords ***
User Set Min Slider Personal Accident On Filter
    [Arguments]  ${value}
    Set Min Slider Personal Accident  ${value}

User Expand The Filter Options
    Expand More Filter Options