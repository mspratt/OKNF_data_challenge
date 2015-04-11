# OKNF_data_challenge
Scrapper for UK data.gov
Data--Challenge

OKFN

I'm writing a scrapper. This project as a great pretext to learn python. It's a learning curve problem and its called :

Get the Data Challenge: Find all the Spending Files

My solution is a more "proof of concept" than finished code. I have a lot to clean up...

Basically the logic flow is (with lots of the little details) in 3 steps

1) I generate this url http://data.gov.uk/api/3/action/organization_list 

Which gives me

"result": ["2gether-nhs-foundation-trust", "aberdeen-city-council", "aberdeenshire-council", "academics",
---------- as an example ---------------------->"adur-district-council", 
"advantage-west-midlands", "advisory-conciliation-and-arbitration-service", "agri-food-and-biosciences-institute", Etc…

so, Publisher title = adur-district-council

Next I generate this url "http://data.gov.uk/api/3/action/organization_show?id=adur-district-council"  

Which returns 

….. "result": {"groups": [ {"capacity": "public", "name": "local-authorities"}], "abbreviation": "", "foi-email": "", "id": "58011ef9-29dc-4729-86e6-82b86d5376ba", "description": "", "category": "local-council", "approval_status": "pending", "title": "Adur District Council", "foi-web": "https://www.whatdotheyknow.com/body/adur_district_council", "users": [

Etc…•
"packages": [

• { • "title": "Allotments", • "id": "b1f2f7be-d024-425f-b6ff-5d8f45d86738", • "name": "allotments46" },

I append to the line “Publisher title” (output file )

Id, type (which I assume is “category”) ?? home page (which I assume is “foi-web”)
and From the “packages” Package title Package id Package name

Next I generate this url http://data.gov.uk/api/3/action/package_show?id=b1f2f7be-d024-425f-b6ff-5d8f45d86738

Which gives me …

"type": "dataset", "resources": [ { "verified_date": "2015-02-10T14:40:05.328921", "hash": "", "description": "Resource locator", "created": "2015-02-10T14:40:05.752325", "url": "http://inspire.misoportal.com/geoserver/adur_and_worthing_council_allotments/wms?request=getCapabilities", "format": "wms", "verified": "True", "tracking_summary": {"total": 0, "recent": 0}, "resource_locator_function": "information", "resource_locator_protocol": "", "ckan_recommended_wms_preview": "True", "position": 0, "revision_id": "e1fb3ea3-44b2-4dc0-94f6-b09e828142d2", "wms_base_urls": "http://inspire.misoportal.com:80/geoserver/adur_and_worthing_council_allotments/ows", "id": "da6e91fe-4fe7-4442-9382-4ac5a402bada", "name": "INSPIRE View Service"},

I append to output Id, category, foi-web, package title, id, name (output file ),  created url id
