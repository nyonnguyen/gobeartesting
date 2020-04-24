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

Click On Filter Option
    [Arguments]  ${option}
    Select Filter Option  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE}  ${option}

Expand More Filter Options
    Wait Until Element Is Visible  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_BUTTON}
    Select Element  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_BUTTON}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_MORE}

Set Min Slider Personal Accident
    [Arguments]  ${value}
    Set Min Slider  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_MORE}  Personal Accident  ${value}
    Wait Until Loaded

Set Max Slider Trip Cancellation
    [Arguments]  ${value}
    Set Max Slider  ${TRAVEL_RESULT_DB_FILTER_COLLAPSE_MORE}  Trip Cancellation  ${value}
    Wait Until Loaded

Top Nav Should Match
    [Arguments]  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${date}
    ${expected_string}  Format String  ${TRAVEL_RESULT_VALIDATE_FORMAT}  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${date}
    Text Should Be Equal  ${TRAVEL_RESULT_NAV_DATA}  ${expected_string}