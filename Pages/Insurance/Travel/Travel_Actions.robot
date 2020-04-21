*** Settings ***
Library           GoBearCore
Resource          ./Travel_Variables.robot

*** Keywords ***
Navigate To Travel Tab
    Select Element  ${TRAVEL_LINK}

Travel Tab Should Be Appeared
    Tab Should Be Active  ${TRAVEL_PANEL}

Set Trip Type
    [Arguments]  ${trip_type}
    Select Button Dropdown  ${TRAVEL_TRIP_TYPE}  ${trip_type}

Set Traveller
    [Arguments]  ${traveller}
    Select Button Dropdown  ${TRAVEL_TRAVELLER}  ${traveller}

Set Travel From Place
    [Arguments]  ${place}
    Select Button Dropdown  ${TRAVEL_FROM_PLACE}  ${place}

Set Travel Start Date
    [Arguments]  ${startdate}
    Set Date  ${TRAVEL_STARTDATE}  ${startdate}

Set Travel End Date
    [Arguments]  ${enddate}
    Input Text  ${TRAVEL_ENDDATE}  ${enddate}

Click Travel Show Result Button
    Select Element  ${TRAVEL_SHOW_RESULT_BUTTON}

Click Travel Reset Button
    Select Element  ${TRAVEL_RESET_FORM}