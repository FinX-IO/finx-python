# FinX Python SDK Testing Instructions

1. Clone this repository

```bash
#! bin/bash
cd ~/
git clone git@github.com:FinX-IO/finx-python
```

2. Have your FinX API Key ready

3. Run the tests directly from the command line

```bash
#! bin/bash
cd ~/finx-python/tests/tick-client
python3 -m functions_test.py # you will be prompted for your FinX API Key
python3 -m streaming_test.py # you will be prompted for your FinX API Key
cd ~/finx-python/tests/calcs
python3 -m greeks_test.py # you will be prompted for your FinX API Key
```
