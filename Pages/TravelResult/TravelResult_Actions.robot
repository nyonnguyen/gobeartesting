*** Settings ***
Library           GoBearCore
Resource          TravelResult_Variables.robot

*** Keywords ***
Travel Result Page Should Be Visible
    Travel Result Top Restul Bar Should Be Visible
    Wait Until Loaded
    Travel Result Filter Should Be Visible
    Travel Result List Should Be Visible

Travel Result Top Restul Bar Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_NAV_DATA}

Travel Result List Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_LIST}

Travel Result Filter Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER_OPTIONS}

Expand More Filter Options
    Wait Until Element Is Visible  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_BUTTON}
    Select Element  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_BUTTON}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE}

Set Min Slider Personal Accident
    [Arguments]  ${value}
    Set Min Slider  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE}  Personal Accident  ${value}
    Wait Until Loaded

Set Max Slider Trip Cancellation
    [Arguments]  ${value}
    Set Max Slider  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE}  Trip Cancellation  ${value}
    Wait Until Loaded