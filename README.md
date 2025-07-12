# Wholesale Order Form Automation (OFA)

## Problem Statement
As a Wholesale Team member, updates the order form xlsx file must be manually performed before sharing with dispensary partners anywhere between 2-4 times a day. This includes (but not limited to) updating and/or removing products, inventory totals, lab results, and manually applying discounted updates for volume and older products. Not only is it a time-consuming (1.5-3 hours a day) and tedious process, but it’s also prone to human error.

## Solution
OFA will query Acumatica’s API endpoints to gather up-to-date data on what products are available to be sold out of the East Boston distribution warehouse, including lab results, quantities, and build the order form in under 3 minutes.

## Process
OFA will make 9 endpoint calls to Acumatica's API to generate 3 inventory related reports. The data extracted from those downloads are then merged and transformed into one dataset. Once the dataset is complete, it’s then loaded into an xlsx file with additional/final transformations before being emailed to the Wholesale Team and uploaded to a SharePoint folder for easy distribution. OFA gives the Wholesale Team back several hours a week, that's better spent on more imortant tasks, such as customer engagement and market research. 
