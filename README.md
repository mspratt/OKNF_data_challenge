# OKNF_data_challenge
Scrapper for UK data.gov
Data--Challenge

OKFN

I'm writing a scrapper. This project as a great pretext to learn python. It's a learning curve problem and its called :
Get the Data Challenge: Find all the Spending Files

My solution is a more "proof of concept" than finished code. I have a lot to clean up...

Run 1st
data_gov_publishers.py  and then 
data_gov_packets.py  (see the code, for the moment they are stand alone, so I can test them)
look in the subdirectory where you ran the programs for the different output files.

Basically the logic flow is (with lots of the little details) in 3 steps

1) I generate this url http://data.gov.uk/api/3/action/organization_list 

Which gives me



Next I generate this url "http://data.gov.uk/api/3/action/organization_show?id=adur-district-council"  

Which returns 


I append to the line “Publisher title” (output file )

Id, type (which I assume is “category”) ?? home page (which I assume is “foi-web”)
and From the “packages” Package title Package id Package name

Next I generate this url http://data.gov.uk/api/3/action/package_show?id=b1f2f7be-d024-425f-b6ff-5d8f45d86738

Which gives me …



I append to output Id, category, foi-web, package title, id, name (output file ),  created url id
