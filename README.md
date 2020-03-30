Tested on MacOS and Ubuntu Server 18.04

Install Dependencies as per ```reqs.txt``` inside a Virtual Environment.

Create a ```vars.py``` file and complete the following variables:

```
api = ""
auth = ""
db = ""
bucket = ""
username = ""
password = ""

```


Run ```python test.py``` to ensure it runs correctly.

To automate speedtests, setup a cronjob. 

Eg, 

```0,30 * * * * /home/huis/jobs/speedtest/venv/bin/python3 /home/huis/jobs/speedtest/test/script.py```