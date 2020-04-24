*** Settings ***
Library           GoBearCore
Resource          ./Travel_Actions.robot

*** Keywords ***
User Should See Travel Tab
  Travel Tab Should Be Appeared

User Navigate To Travel Tab
  Navigate To Travel Tab
  Travel Tab Should Be Appeared

User Click Show Travel Result Button
    Click Travel Show Result Button