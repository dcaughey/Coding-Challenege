# Coding-Challenge
Repo for the South SE Coding Challenge

Why: I have a customer who has invested heavely in both traditonal Cisco gear and Meraki for a subset of their branch environments. We helped them build some scripting functionality to make building out their Meraki deployment easier to manage and provide the visibility thier customers we asking for into the network.

What: This simple applications takes input from a .csv file to "auto-magically" add devices (listed in the csv file) to the Meraki Dashboard.  The devices will be added to a new or existing network, so depending upon if this is an initial installation or simply adding additional gear to an existing site both are allowed! In the Meraki world, the serial number of a device is used to "claim" a device into an organization and placed into a site or network.  The .csv file in this example is very simple, the Meraki APIs allow for a large amount of instrumentation and functionality and this a somewhat basic "on-boarding" script.

The .cvs file is expected to be named "MerakiInventory.csv" and contains the site or network, device model, serial number and "working name", below is the actual data within the file.

network,device,serial-no,name

site01,MX60,Q2BN-6FFY-D5X9,Old MX60

site01,MR24,Q2ED-CKGM-MP6V,Old MR24

Dependancies:
The script expects a file named vars.py to be present in the working directory and this file contains the API-Key or token and Org-Id which provides access to the the Meraki dashboard organization.  This information "should NOT" shared outside of your organization because bad things could happen if a hacker got a hold of this key.  I've posted the file in this repository but have removed my token information for security reasons!

Execution: 
This python script was written for pyton 2.7, to run the script place the .cvs file and the vars.py files into a sub-directory structure that is known to python and type "python Meraki-Inv.py"

Output:
The script will output progress messages as it works it's way thru the process and indicate the number of devices processed at conculsion!

Test-Programs dcaughey1$ python Meraki-Inv.py

Adding the device 'MX60' with serial# 'Q2BN-6FFY-D5X9' and named 'Old MX60' in network 'site01'
  Successfully added New network 'site01' to Organization  
    Add/Claim Device Serial# 'Q2BN-6FFY-D5X9' to site/network 'site01'    
    Updated Device with local name 'Old MX60' and device name 'MX60' in notes fields

Adding the device 'MR24' with serial# 'Q2ED-CKGM-MP6V' and named 'Old MR24' in network 'site01'
  Network 'site01' exists adding device  
    Add/Claim Device Serial# 'Q2ED-CKGM-MP6V' to site/network 'site01'    
    Updated Device with local name 'Old MR24' and device name 'MR24' in notes fields
    
Script completed successfully, Processed 2 devices


