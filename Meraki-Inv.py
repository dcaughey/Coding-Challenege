#!/usr/bin/env python2.7
import json
import pprint
import requests
import csv
from StringIO import StringIO
from vars import apikey, orgId

with open('MerakiInventory.csv', mode='r') as csv_file:
    line_count = 0
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        csv_network = row['network']
        csv_device = row['device']
        csv_serial_no = row['serial-no']
        csv_name = row['name']
        print "\nAdding the device '{}' with serial# '{}' and named '{}' in network '{}'".format(csv_device, csv_serial_no, csv_name, csv_network)

        line_count += 1

        # Add a Network to an existing Org. Name came from the csv file
        url1 = "https://api.meraki.com/api/v0/organizations/"+orgId+"/networks"
        payload = {
            'name' : csv_network,
            'type' : "wireless  switch",
            'timeZone' : "America/New_York",
            'tags': "test-tag"
            }
        string=json.dumps(payload)

        headers = {
            'x-cisco-meraki-api-key': apikey,
            'content-type': "application/json"
            }

        response = requests.request("POST", url1, data=string, headers=headers)
        if response.status_code == 201:
            print "  Successfully added New network '{}' to Organization".format(csv_network)
            resp_dict = response.json()
            new_network_id = resp_dict['id']
        elif response.status_code == 400:
            print "  Network '{}' exists adding device".format(csv_network)


        # Claim a device to this network
        url2 = "https://dashboard.meraki.com/api/v0/networks/"+new_network_id+"/devices/claim"
        payload = {
            'serial' : csv_serial_no
            }
        string=json.dumps(payload)
        headers = {
            'x-cisco-meraki-api-key': apikey,
            'content-type': "application/json"
            }

        response = requests.request("POST", url2, data=string, headers=headers)
        print "    Add/Claim Device Serial# '{}' to site/network '{}'".format(csv_serial_no, csv_network)

        #Update the device information - Add the local name from the csv csv_file
        url2 = "https://dashboard.meraki.com/api/v0/networks/"+new_network_id+"/devices/"+csv_serial_no
        payload = {
            'name' : csv_name,
            'notes' : csv_device
            }
        string=json.dumps(payload)
        headers = {
            'x-cisco-meraki-api-key': apikey,
            'content-type': "application/json"
            }

        response = requests.request("PUT", url2, data=string, headers=headers)

        print "    Updated Device with local name '{}' and device name '{}' in notes fields".format(csv_name, csv_device)

    print "\nScript completed successfully, Processed {} devices".format(line_count)
