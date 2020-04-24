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

User Click On Filter Option
    [Arguments]  ${option}
    Click On Filter Option  ${option}
    Wait Until Loaded

The '${count_result} plans found ${trip_type} | for ${traveller} | travel to ${place} | from ${date}' Should Be Displayed
    Top Nav Should Match  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${date}