*** Settings ***
Library           GoBearCore
Resource          ../Pages/Travel/Travel_Page.robot
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
    Set Travel Start Date  12-Jun-2024
    Click Travel Show Result Button
    sleep  5