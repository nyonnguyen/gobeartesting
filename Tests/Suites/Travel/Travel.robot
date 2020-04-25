*** Settings ***
Library           GoBearCore
Resource          ../Tests/Base_Test.robot
Resource          ../Pages/Travel/Travel_Page.robot
Resource          ../Pages/TravelResult/TravelResult_Page.robot
Variables         ../Tests/Data/Travel/Travel.yaml

Test Setup       User Prepare The Test Environment

Test Teardown    User Cleanup The Test Environment

*** Test Cases ***

User Can Search For Travel Insurance
    [Tags]  test1  search
    Given User Navigate To Travel Tab
    When Set Trip Type  ${TEST1.TRIP_TYPE}
    And Set Traveller  ${TEST1.TRAVELER}
    And Set Travel From Place  ${TEST1.TRAVEL_PLACE}
    And Set Travel Start Date  ${TEST1.TRAVEL_DATE}
    And User Click Show Travel Result Button
    Then User Should See Travel Result Page
    And '${TEST1.TRAVEL_RESULT} plans found ${TEST1.TRIP_TYPE} | for ${TEST1.TRAVELER} | travel to ${TEST1.TRAVEL_PLACE} | from ${TEST1.TRAVEL_DATE}' Should Be Displayed

User Can Filter Travel Insurance
    [Tags]  test2  filter
    [Setup]  User Is In Search Travel Result Page
    When User Expand The Filter Options
    And User Select Filter Option  ${TEST2.FILTER_OPTION}
    And User Set Min Slider Personal Accident On Filter  ${TEST2.FILTER_ACCIDENT}
    And User Set Max Slider Trip Cancellation  ${TEST2.FILTER_CANCELLATION}
    Then '${TEST2.TRAVEL_RESULT} Travel Cards' Should Be Found At Least

User Can Set Detail Travel Insurance At Travel Result Page
    [Tags]  test3  filter
    [Setup]  User Is In Search Travel Result Page
    When User Select Filter Sort Option  ${TEST3.FILTER_SORT}
    And User Filter By Detail Policy Type  ${TEST3.DETAIL_POLICY}
    And User Filter By Detail Traveller  ${TEST3.DETAIL_TRAVELER}
    And User Select Filter Destination  ${TEST3.FILTER_DESTINATION}
    And User Set Filter Start Date  ${TEST3.FILTER_START_DATE}
    And User Set Filter End Date  ${TEST3.FILTER_END_DATE}
    Then '${TEST3.TRAVEL_RESULT} Travel Cards' Should Be Found

*** Keywords ***

User Is In Search Travel Result Page
    User Prepare The Test Environment
    User Navigate To Travel Tab
    User Click Show Travel Result Button
    User Should See Travel Result Page