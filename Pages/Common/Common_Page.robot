*** Settings ***
Library           GoBearCore
Resource          ./Common_Actions.robot

*** Keywords ***
User Should See The Insurance
    Insurance Should Be Visible

User Navigate To Insurance Tab
    Navigate To Insurance