"""
data_gov_publishers.py

This program access the http://data.gov.uk/api/ in order to
scrap the list of publishers. the returned data is in json
format.

Using the names obtained from the publisher's
list we create a new url string by concatenating 
"http://data.gov.uk/api/3/action/organization_show?id="
with the publisher_name.

With this new querry we then access the site again and save
the publsiher's data to new json file.
We read through the new json file on "packages in order to get the
title, id and name of the publication.

We then create the output file

the application is divided (for the moment) into 3 seperate python files
data_gov_publishers
                   data_gov_packets
                                   data_gov_output
   
Do these changes showup in GIT??  YES they did
whoooo -cool !!  super cool - no?

where is the version no?  - it show up in the committed list

"""


#*************************************************
#  Initialize
import sys, os, urllib3, json, html
import data_gov_packets

#*********************   get the orgainsation list

url_0 = "http://data.gov.uk/api/3/action/organization_list"
http_0= urllib3.PoolManager()
page_returned_0 = http_0.request('GET', url_0)

#print("page returned=", page_returned_0)
#print("page status  =", page_returned_0.status)
print("    ")
f = open("organization_list.json", 'wb')
f.write(page_returned_0.data)


with open('organization_list.json') as data_file_0:    
    organization_data = json.load(data_file_0)



# *******************  loop through publisher   ******
print("********   loop through publishers   ************")
cntr=0
for x in organization_data["result"] :
     if cntr > 5:  # get only the first 5 publishers
         break

     publisher_name = organization_data["result"][cntr]
 
     url_1 = "http://data.gov.uk/api/3/action/organization_show?id="+ publisher_name
     http_1 = urllib3.PoolManager()
     publisher_returned = http_1.request('GET', url_1)

     print("publisher number=", cntr)
     print("publisher name  =", publisher_name)
     print("page status     =", publisher_returned.status)
     #print("page returned   =", publisher_returned )
     #print("page data=",(publisher_returned.data))
     print("    ")


     #****************************************
     #  read the save json file
     f_1 = open(publisher_name + ".json", 'wb')
     f_1.write(publisher_returned.data)

     cntr += 1

     #********************************
     #  go read through all the packets
     #  for this publisher
     
     #if __name__ == '__main__': 
     python data_gov_packets

     #os.system("data_gov_packets.py")
     #********************************
     # delete the current publisher file
     #
     #  But, not yet there are only 5
     
     
