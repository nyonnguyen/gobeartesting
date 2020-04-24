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

User Select Filter Option
    [Arguments]  ${option}
    Click On Filter Option  ${option}
    Wait Until Loaded

User Select Filter Sort Option
    [Arguments]  ${option}
    Click On Sort Option  ${option}
    Wait Until Loaded

User Filter By Detail Policy Type
    [Arguments]  ${policy}
    Set Detail Policy Type  ${policy}

User Filter By Detail Traveller
    [Arguments]  ${traveller}
    Set Detail Traveller Value  ${traveller}

User Select Filter Destination
    [Arguments]  ${destination}
    Select Detail Destination Value  ${destination}

User Set Filter Start Date
    [Arguments]  ${date}
    Set Detail Start Date  ${date}

User Set Filter End Date
    [Arguments]  ${date}
    Set Detail End Date  ${date}

'${count_result} plans found ${trip_type} | for ${traveller} | travel to ${place} | from ${date}' Should Be Displayed
    Top Nav Should Match  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${date}

Another '${count_result} plans found ${trip_type} | for ${traveller} | travel to ${place} | from ${startdate} to ${enddate}' Should Be Displayed
    Top Nav Should Match With End Date  ${count_result}  ${trip_type}  ${traveller}  ${place}  ${startdate}  ${enddate}