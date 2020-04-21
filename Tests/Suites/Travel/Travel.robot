*** Settings ***
Library           GoBearCore
Resource          ../Pages/Insurance/Travel/Travel_Page.robot
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
    Set Travel Start Date  30-05-2020
#    Click Travel Show Result Button
    sleep  5