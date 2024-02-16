# osha.gov-Scraper
Scrape Injury data of this website  https://www.osha.gov/ords/imis/industry.html


## Client Requirements
Crawl through this list - https://www.osha.gov/ords/imis/industry.html

following filters applied:
- start date: 01/01/2023
- end date: today
- NAICS: 31

For each activity, if it has a violation, drill in and collect this info if one of the listed violations has ""5A0001"" for Standard Cited. Build an array of json objects. Each object is an inspection, with a nested array of violation objects.

Scrape all inspections:
- Establishment name
- ST
- Inspection Nr:
- case status:
- inspection information - office:
- Report ID:
- Date Opened:
- Site Address:
- Mailing Address:
- union status
- SIC
- NAICS:
- Inspection Type:
- Scope:
- Advanced Notice:
- Ownership:
- Safety/Health:
- Close Conference:
- Emphasis:
- Case Closed:
- violations (nested json object)
- violation items with Standard Cited ""5A0001""
- for only violations with 5A0001, pull:
- ""Hazard"" text (we'll use this to search for ""MSD"", ""strain"", ""musculoskeletal"", ""exertion"", ""%ergo%"", etc.) to flag as ergonomics
- citation type
- Current Penalty
- Initial Penalty
- fta penalty
- citation type
- issuance date
- contest
- abatement due date
