*** Settings ***
Library     GoBearCore
Resource  ../Utilities/Utils.robot
Resource  ../Pages/Common/Common_Page.robot
Variables  Data/settings.yaml

*** Keywords ***
User Open Browser And Go To Webview
  [Arguments]  ${URL}
  Setup Browser
  Go To    ${URL}

Setup Browser
  ${settings} =  Convert To Dictionary  ${BROWSER}
  Setup Browser Driver  ${settings}

User Prepare The Test Environment
  User Open Browser And Go To Webview  ${WEB_URL}
  User Should See The Insurance
  User Navigate To Insurance Tab

User Cleanup The Test Environment
  Capture Page Screenshot
  Close Browser

#User Cleanup Test Case
#  Capture Page Screenshot

