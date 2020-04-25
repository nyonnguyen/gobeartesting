*** Settings ***
Library           GoBearCore
Resource          TravelResult_Variables.robot

*** Keywords ***
Travel Result Page Should Be Visible
    Travel Result Top Restul Bar Should Be Visible
    Wait Until Loaded
    Travel Result Filter Should Be Visible
    Travel Result List Should Be Visible
    Travel Result Filter Detail Should Be Visible

Travel Result Top Restul Bar Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_NAV_DATA}

Travel Result List Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_LIST}

Travel Result Filter Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER_OPTIONS}

Travel Result Filter Detail Should Be Visible
    Wait Until Element Is Visible  ${TRAVEL_RESULT_DETAIL_COLLAPSE}

Click On Filter Option
    [Arguments]  ${option}
    Select Filter Option  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE}  ${option}

Click On Sort Option
    [Arguments]  ${option}
    Select Sort Option  ${TRAVEL_RESULT_SB_SORT_BAR}  ${option}

Expand More Filter Options
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE_BUTTON}
    Select Element  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE_BUTTON}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE}
    Wait Until Element Is Visible  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE_MORE}

Set Min Slider Personal Accident
    [Arguments]  ${value}
    Set Min Slider  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE_MORE}  Personal Accident  ${value}
    Wait Until Loaded

Set Max Slider Trip Cancellation
    [Arguments]  ${value}
    Set Max Slider  ${TRAVEL_RESULT_SB_FILTER_COLLAPSE_MORE}  Trip Cancellation  ${value}
    Wait Until Loaded

Set Detail Policy Type
    [Arguments]  ${policy}
    Select Detail Option  ${TRAVEL_RESULT_DETAIL_COLLAPSE}  ${policy}
    Wait Until Loaded

Set Detail Traveller Value
    [Arguments]  ${traveller}
    Select Detail Option  ${TRAVEL_RESULT_DETAIL_COLLAPSE}  ${traveller}
    Wait Until Loaded

Select Detail Destination Value
    [Arguments]  ${destination}
    Select Button Dropdown  ${TRAVEL_RESULT_FILTER_DESTINATION}  ${destination}
    Wait Until Loaded

Set Detail Start Date
    [Arguments]  ${date}
    Set Date  ${TRAVEL_RESULT_FILTER_START_DATE}  ${date}
    Wait Until Loaded

Set Detail End Date
    [Arguments]  ${date}
    Set Date  ${TRAVEL_RESULT_FILTER_END_DATE}  ${date}
    Wait Until Loaded

Top Nav Should Match
    [Arguments]  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${date}
    ${expected_string}  Format String  ${TRAVEL_RESULT_VALIDATE_FORMAT}  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${date}
    Text Should Be Equal  ${TRAVEL_RESULT_NAV_DATA}  ${expected_string}

Top Nav Should Match With End Date
    [Arguments]  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${startdate}  ${enddate}
    ${expected_string}  Format String  ${TRAVEL_RESULT_VALIDATE_WITH_DATE_FORMAT}  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${startdate}  ${enddate}
    Text Should Be Equal  ${TRAVEL_RESULT_NAV_DATA}  ${expected_string}

Number Found Travel Cards Should Be Matched
    [Arguments]  ${expected_count}
    Number Of Found Elements Should Be  ${TRAVEL_RESULT_PLAN}  ${expected_count}  Number Travel Cards is not matched

Number Found Travel Cards Should At Least
    [Arguments]  ${expected_count}
    Number Of Found Elements Should At Least  ${TRAVEL_RESULT_PLAN}  ${expected_count}  Number Travel Cards is not matched