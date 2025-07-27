# Wholesale Order Form Automation (OFA)

## Problem Statement
As a Wholesale Team member, updates to the order form xlsx file must be manually performed before sharing with dispensary partners anywhere between 2-4 times a day. This includes (but not limited to) updating and/or removing products, inventory totals, lab results, and manually applying discounted pricing for volume and older products. Not only is it a time-consuming (1.5-3 hours a day) and tedious process, but it’s also prone to human error - especially when applying volume discounts to the spreadsheet after a long day on the road.

## Solution
OFA is an automated Python (v3.12.6) solution that lives on a Windows VM hosted on an AWS EC2 instance. OFA runs on an AWS EventBridge schedule, 6 times a day, and completely takes order form management off of the Wholesale Team's to-do list. OFA gives the Wholesale Team back several hours a week, that's better spent on more imortant tasks, such as customer engagement and market research.

## Process
OFA will query Acumatica’s API endpoints to extract up-to-date data on product availability in the East Boston distribution warehouse, including lab results, quantities, merge and transform the data from the 3 extractions, then build the order form with applicable dynamic pricing formulas for volume in under 4 minutes.

OFA is a fully automated ETL pipeline that runs on an AWS EventBridge schedule that makes 6 endpoint calls to Acumatica's API to generate 3 inventory related reports. The data extracted from those downloads are then merged and transformed into one dataset. Once the dataset is complete, it’s then loaded into an xlsx file with additional/final transformations before being emailed to the Wholesale Team and uploaded to a SharePoint folder for easy distribution.

## Portfolio Notes
- While this project isn't your typical data pipeline, I wanted to feature this project to demonstrate my transformation chops, both within dataframes and excel. 
- I have stripped out endpoints and other sensitive detials from the automation, so you can't download and run this. But I am more than happy to demonstrate this for you! :) 
