# Wholesale Order Form Automation (OFA)

## The Wholesale Order Form (Former) Process

As part of the Wholesale Team’s former daily routine, they update a long standing xlsx file that is distributed to dispensary partners as an order form. 

The order form is a list of products Happy Valley currently has available in stock with inventory totals, lab results, and pricing. The order form also contains typical fields/columns such as “Order Quantity” and “Total” for each line item with supporting formulas so if you order 10 cases of an item that costs $10 per case, the total cost for that line item is $100. With an Order Total field at the bottom of the Total column, which sums up the dollar total in that column. 

In order to provide up to date quantities, lab results, etc a wholesale team member would log into their ERP and navigate to the appropriate pages that contains all of this information (a page for products already in the distribution warehouse and another page for products in-transit from the production facility to the distribution warehouse) and manually update quantity, lab results, and add or remove products from the order form. The order form would be prepped in this manner 2-4 times a day to ensure quantities, etc are up to date (due to orders being processed and product quantities updating). 

Then when an order form is sent back from a customer, a wholesale team member would have to apply volume discounts when appropriate when placing the order into the ERP. 
## Problem Statement
As a Wholesale Team member, updates to the order form xlsx file must be manually performed before sharing with dispensary partners anywhere between 2-4 times a day. This includes (but not limited to) updating and/or removing products, inventory totals, lab results, and manually applying discounted pricing for volume and older products. Not only is it a time-consuming (1.5-3 hours a day) and tedious process, but it’s also prone to human error - especially when applying volume discounts to the spreadsheet after a long day on the road.

## Solution
OFA is an automated Python (v3.12.6) solution that lives on a Windows VM hosted on an AWS EC2 instance. OFA runs on an AWS EventBridge schedule, 6 times a day, and completely takes order form management off of the Wholesale Team's to-do list. OFA gives the Wholesale Team back several hours a week, that's better spent on more imortant tasks, such as customer engagement and market research.

## Process
OFA will query Acumatica’s API endpoints to extract up-to-date data on product availability in the East Boston distribution warehouse, including lab results, quantities, merge and transform the data from the 3 extractions, then build the order form with applicable dynamic pricing formulas for volume in under 4 minutes.

OFA is a fully automated ETL pipeline that runs on an AWS EventBridge schedule that makes 6 endpoint calls to Acumatica's API to generate 3 inventory related reports. The data extracted from those downloads are then merged and transformed into one dataset. Once the dataset is complete, it’s then loaded into an xlsx file with additional/final transformations before being emailed to the Wholesale Team and uploaded to a SharePoint folder for easy distribution.

## Notes
- While this project isn't your typical data pipeline, I wanted to feature this project to demonstrate my transformation chops, both within dataframes and excel. 
- I have stripped out endpoints and other sensitive detials from the automation, so you can't download and run this. But I am more than happy to demonstrate this for you! :) 
