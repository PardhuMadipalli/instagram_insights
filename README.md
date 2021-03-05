![](https://github.com/PardhuMadipalli/instagram-insights/workflows/Publish%20PyPi%20Package/badge.svg)

[![codecov](https://codecov.io/gh/PardhuMadipalli/instagram-insights/branch/main/graph/badge.svg?token=SJ6F03WTTK)](https://codecov.io/gh/PardhuMadipalli/instagram-insights)

#### Partial report screenshot

![Report Screenshot](screenshot.png "Report Screenshot")

## Quickstart

1. Install the package using:<br>
`pip install instagram-insights`

2. Run the python scripts using:<br>
`insta-insights --page-id=124567890123 --token=098754321234567890 --num-timings=2 --num-tags=3`

- Page ID and Token must be provided either as options or environment variable values. 
- If both options and env variables are provided options will be preferred.

#### Options supported

| Short options | Long options | Environment variables | Description |
|---------------|--------------|-----------------------|-------------|
| -h | --help | | Display help |
| -m | --machine-learning | | Whether to use ML or not (currently not supported)|
| | --page-id | FB_PAGE_ID| Instagram Page ID |
| | --token   | FB_TOKEN  | Token to access Facebook Graph API |
| | --num-timings | | Number of best timings needed |
| | --num-tags | | Number of best hashtags needed |
| | --graphs | | Whether to generate graphs or not |


#### Python version

- \>= 3.7

#### Packages needed
- numpy
- pandas
