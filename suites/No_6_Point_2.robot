*** Settings ***
Library         RequestsLibrary
Library         String
Library         HttpLibrary.HTTP
Library         Collections 
Library         OperatingSystem
Library         Selenium2Library  

*** Variables ***
${url_api_efishery}     https://stein.efishery.com
*** Keywords *** 
API PA Jadwal Dokter
       CreateSession        detail       ${url_api_efishery}             verify=True

       ${header}=      Create Dictionary       Content-Type=application/json        
       
       ${resp}=     Get Request        detail           /v1/storages/5e1edf521073e315924ceab4/list          headers=${header}
       Should Be Equal As Strings	${resp.status_code}	200
       	
       ${jsondata}=  To Json  ${resp.content}

        ${count} =     set variable   ${0}

            FOR  ${h}  IN  @{jsondata}
                ${found}=    Run Keyword and Return Status        Dictionary Should Contain Value      ${h}     BULELENG
                ${count}=    Set variable if     ${found}      ${count+1}    ${count}
            END
            Log     ${count}   WARN
*** Test Cases ***
Login Jadwal Dokter
    API PA Jadwal Dokter

                   
                   
