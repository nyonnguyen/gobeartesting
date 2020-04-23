*** Settings ***
Library           GoBearCore
Resource          ../Pages/Travel/Travel_Page.robot
Resource          ../Pages/TravelResult/TravelResult_Page.robot
Resource          ../Tests/Base_Test.robot

Suite Setup       User Prepare The Test Environment

Suite Teardown    User Cleanup The Test Environment

*** Test Cases ***

User Can Navigate To Travel Tab
    [Tags]  test
    User Navigate To Travel Tab
    Set Trip Type  annual trip
    Set Traveller  5 persons
    Set Travel From Place  Asia
    Set Travel Start Date  12-December-2026
    Click Travel Show Result Button

    User Should See Travel Result Page
    User Expand The Filter Options
    User Set Min Slider Personal Accident On Filter  1567800
    User Set Max Slider Trip Cancellation  50000