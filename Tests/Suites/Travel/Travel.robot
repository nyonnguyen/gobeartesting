*** Settings ***
Library           GoBearCore
Resource          ../Pages/Travel/Travel_Page.robot
Resource          ../Pages/TravelResult/TravelResult_Page.robot
Resource          ../Tests/Base_Test.robot

Test Setup       User Prepare The Test Environment

Test Teardown    User Cleanup The Test Environment

*** Test Cases ***

User Can Search For Travel Insurance
    [Tags]  test1
    Given User Navigate To Travel Tab
    When Set Trip Type  annual trip
    And Set Traveller  5 persons
    And Set Travel From Place  Asia
    And Set Travel Start Date  12 Dec 2026
    And User Click Show Travel Result Button
    Then User Should See Travel Result Page
    And '12 plans found annual trip | for 5 persons | travel to Asia | from 12 Dec 2026' Should Be Displayed

User Can Filter Travel Insurance
    [Tags]  test2
    [Setup]  User Is In Search Travel Result Page
    When User Expand The Filter Options
    And User Select Filter Option  Pacific Cross
    And User Set Min Slider Personal Accident On Filter  1500000
    And User Set Max Slider Trip Cancellation  50000
    Then Another '6 plans found single trip | for me | travel to Hong Kong | from 01 May 2020 to 10 May 2020' Should Be Displayed

User Can Set Detail Travel Insurance At Travel Result Page
    [Tags]  test3
    [Setup]  User Is In Search Travel Result Page
    When User Select Filter Sort Option  Price: Low to high
    And User Filter By Detail Policy Type  single trip
    And User Filter By Detail Traveller  3 persons
    And User Select Filter Destination  Singapore
    And User Set Filter Start Date  30 April 2020
    And User Set Filter End Date  7 May 2020
    Then Another '22 plans found single trip | for 3 persons | travel to Singapore | from 30 Apr 2020 to 07 May 2020' Should Be Displayed


*** Keywords ***

User Is In Search Travel Result Page
    User Prepare The Test Environment
    User Navigate To Travel Tab
    User Click Show Travel Result Button
    User Should See Travel Result Page