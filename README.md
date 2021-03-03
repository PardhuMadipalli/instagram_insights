
#### Partial report screenshot

![Report Screenshot](screenshot.png "Report Screenshot")

## Quickstart

1. Install the package using:<br>
`pip install instagram-insights`

2. Run the python scripts using:<br>
`insta-insights --page-id=124567890123 --token=098754321234567890`

- Page ID and Token must be provided either as options or environment variable values. 
- If both options and env variables are provided options will be preferred.

#### Options supported

| Short options | Long options | Environment variables |
|---------------|--------------|-----------------------|
| -h | --help ||
| -m | --machine-learning ||
| | --page-id | FB_PAGE_ID|
| | --token   | FB_TOKEN  |


#### Python version

- \>= 3.6

#### Packages needed
- numpy
- pandas
