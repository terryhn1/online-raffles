# Online Raffle Handler

Due to the concerns of COVID-19, most events will most likely go online. Most CKI big fundraising events require raffling in order to draw more people to attend the events. However, a situation comes up with online raffling as by doing it manually, a stress-free user experience is not possible. Raffles have to be done 1 by 1 and response forms must be checked continuously for updates.

Therefore, to eliminate the stressful work that may come with setting up raffles, this code
  - provides a user-friendly experience for the one in charge of raffling and the one buying raffles
  - encourages users to use a Google Forms template with the basic necessities and structure.
  - prevents high usage time and confusion for buying raffles.
  - associates each person with the base of their email so same names do not become an issue.
  
This code uses the Google Sheets API in order to provide a connection between the Google Sheets response form for raffles.

## Instructions on how to use the Code

### Step 1
Create a Google Form using the template: [Sample Response Form](https://docs.google.com/spreadsheets/d/1RUxgSFgkED1AJzY_pKu4HLdCMCDRGGOKlYSIV9249wI/edit?usp=sharing).
To do so, go to the top and find "Forms". From Forms, you should click "Edit Forms" to make your own version of the form. Follow the format of the form by only adding in prizes and nothing else.
Create an empty Google Sheets that will be used for the resulting file in which you can use to determine the winner of your raffle. 

### Step 2
Make sure you have the latest Python installed. I encourage to download pip too, but you can run the code through Python's IDLE editor.

### Step 3
Visit the [Google Sheets API Quickstart](https://developers.google.com/sheets/api/quickstart/python) website and follow Step 1 and 2. You will be downloading the necessary libraries and activating the Google Sheets API authentication for your account.

### Step 4
In **main.py**, there will be a fill-in section. In this section, you will need to find out the ID of the Google Sheets Form. One of the ID's will be a Google Sheet that collected the responses for the raffles and another one should just be an empty Google Sheets file.
For example, the ID of https://docs.google.com/spreadsheets/d/1RUxgSFgkED1AJzY_pKu4HLdCMCDRGGOKlYSIV9249wI/edit#gid=627206459 is 1RUxgSFgkED1AJzY_pKu4HLdCMCDRGGOKlYSIV9249wI.

### Step 5
Continuing in **main.py** in the fill-in section. You will need to update the list variables _ranges_ and _prizes_. You can find the named ranges by choosing a block of data on the Google Sheets and giving it a unique name or using the default name(which is used in the code). When updating, take into account the last column(the column letter of your last prize) on the Response sheet.

### Step 6
Run code using pip or IDLE. I use Git Bash on a Windows 10, so my command is "python main.py". After that, you're done! Use a random number selector to find the winner of your raffle.

## Further Implementation
Depending if it is needed, I will be considering creating an automatic email response that calculates the total price of the raffles bought. Otherwise, I believe this should be solved by manual work of the leader in charge of raffles.

