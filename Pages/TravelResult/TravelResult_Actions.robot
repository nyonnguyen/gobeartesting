*** Settings ***
Library           GoBearCore
Resource          TravelResult_Variables.robot

*** Keywords ***
Travel Result Page Should Be Visible
    wait until element is visible  ${TRAVEL_RESULT_NAV_DATA}

Expand More Filter Options
    Select Element  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_BUTTON}

Set Min Slider Personal Accident
    [Arguments]  ${value}
    Set Min Slider  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE}  Personal Accident  ${value}