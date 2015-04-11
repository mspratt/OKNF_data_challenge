"""
data_gov_packets.py

This program is the 2nd of 3
you got here from data-gov-publisher

Thus, we have a publisher's name and
want to get the list of their publications


"""
#*************************************************
#  Initialize
import sys, os, urllib3, json, html
#import data_gov_output


#*************************************
#  We have a department/publisher
#  what have they got on-line?
#
#  select a large publisher for testing
with open("adur-district-council.json") as data_file_2: 
     publisher_data = json.load(data_file_2)
    
#with open(publisher_returned) as data_file_2: 
#  publisher_data = json.load(data_file_2)


#************************************
#  loop throught the results.packages
#  of the publisher's page and
#  get the title, id and name

# ------------------------
#  for testing I've shut down the loop
#  and I'm only printing the
#  1st occurance of results
# ------------------------

cntr_2 = 0
#for cntr_2 in publisher_data["result"]:
      #  if cntr_2 > 5:
      #      break

#****************************************
#  create an output line, element by element
#  next time I'm going to print using
#  just publisher_data["result"]["packages"][0]["title"]


publisher_title = publisher_data["result"]["packages"][cntr_2]["title"]
print("publisher_title = ", publisher_title)

publisher_id = publisher_data["result"]["packages"][cntr_2]["id"]
print("publisher_id = ", publisher_id)

publisher_name= publisher_data["result"]["packages"][cntr_2]["name"]
print("publisher_name = ", publisher_name)

publisher_type = publisher_data["result"]["type"][cntr_2]
print("publisher_type = ", publisher_type)


f = open("data_gov_publisher_results.txt", 'a')

#**************************************************
#  start writing one record with all the required elements

output_line =""
quote = '"'
spacer = '","'
output_line = output_line + quote + publisher_id + spacer

output_line = output_line + publisher_title + spacer
output_line = output_line + publisher_type + spacer
output_line = output_line + publisher_name + spacer


#python data_gov_output

print("********************")


print ("end of for")





