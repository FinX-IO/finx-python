# Installation

## FinX Python SDK

FinX Python SDK is an installable python package registered with PyPi.org and installable as follows:

#### Linux Install

##### latest release

```bash
pip install finx-io
```

##### beta release

```bash
pip install -i https://test.pypi.org/simple/ finx-io
```

#### Mac Install

```mac command line
python3 -m pip install finx-io
```

# FinX API Key

### A FinX API Key is required to use the FinX Python SDK and FinX Webservice Endpoints

> To obtain a FinX API Key, please contact info@finx.io

Your FinX API Key must be set as an environment variable FINX_API_KEY

To set your FINX_API_KEY using _*bash*_:

```bash
#! bin/bash
export FINX_API_KEY='(your api key here)'

# test it
echo $FINX_API_KEY
```

To set your FINX_API_KEY using _*python*_:

```python
#! python
import os
os.environ['FINX_API_KEY'] = '(your api key here)'

# test it
os.getenv('FINX_API_KEY')
```
