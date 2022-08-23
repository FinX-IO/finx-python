# FinX Python SDK

## Python Reference

1. Tick Streamer
2. Tick Snap
3. Tick History
4. Timeslice of Contract Ticks
5. Calculate Greeks
6. Implied Volatility Surface Generator
7. Calculation Grid Function Reference

### Tick Streamer

#### How to Stream Ticks to Console

```python
#! python
import finx
from finx.finx_streamer import Streamer

import os
os.environ['FINX_API_KEY'] = ''

streamer = Streamer(dict(pair='BTC:USDC'))
streamer.connect()
streamer.listen('console')
```

#### How to Stream Ticks to File ('output.txt')

```python
#! python
import finx
from finx.finx_streamer import Streamer

import os
os.environ['FINX_API_KEY'] = ''

streamer = Streamer(dict(pair='BTC:USDC'),"dev")
streamer.connect()
streamer.listen('output.txt')
```

### Tick Snap

#### How to Fetch Tick Snap

```python
#! python
import finx
from finx.tick_client import TickPlant
import os
os.environ['FINX_API_KEY'] = ''

tick_plant = TickPlant("dev")
tick_plant.connect()
tick_snap = tick_plant.tick_snap("BTC:USDC","2022-07-01","00:00")
print(tick_snap)
```

### Tick History

#### How to Fetch Tick History

```python
#! python
import finx
from finx.tick_client import TickPlant
import os
os.environ['FINX_API_KEY'] = ''

tick_plant = TickPlant("dev")
tick_plant.connect()
tick_history = tick_plant.tick_history("BTC:USDC","2022-06-01","00:00")
print(tick_history)
```

### Timeslice of Contract Ticks

### How to Fetch a Timeslice of Contract Ticks

```python
import pandas as pd
import finx
from finx.tick_client import TickPlant
tp = TickPlant()
df = tp.get_timeslice(api_key='my_api_key', timeslice_datestamp='1660825325', timeslice_width_seconds='10', underlying_symbol='BTC')
```

### Calculate Greeks

#### How to Calculate Greeks for a Derivative

```python
#! python
import finx
import os
from finx.client import FinXClient
import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"

finx_api_key = os.getenv('FINX_API_KEY')
finx_api_endpoint = 'https://hedgefunds.finx.io/api/'
finx = FinXClient('socket', finx_api_key=finx_api_key, finx_api_endpoint=finx_api_endpoint, ssl=True)
# s0, k, r, sigma, q, T, p, option_side, option_type
# s0 = spot price
# k = underlying price
# r = risk free rate
# sigma = volatility - if left blank then Implied Volatility will be calculated from option price
# q = coupon rate of the financial instrument
# T = days to strike date
# p (price) = price of option
# option_side = call or put
# option_type = american or european
result = finx.calculate_greeks(s0, k, r, sigma, q, days_left, price, 'call', 'european')
print(result)
```



### Implied Volatility Surface Generator

Calculates an implied volatility surface for a given pair's options given a snapshot in time of observed IV quotes 
for any range of strike prices and expirations.

#### calibrate_vol_surface(params)

##### calibrate_vol_surface: params

```params
{
  "filename": string, 
}
```

*filename* is the submitted existing IV or price observations. Files are submitted via submit_file(params) [0.0.94]

```python
#! python
import finx
import os
from finx.client import FinXClient

finx_api_key = os.getenv('FINX_API_KEY')
finx_api_endpoint = 'https://hedgefunds.finx.io/'
finx = FinXClient('socket', finx_api_key=finx_api_key, finx_api_endpoint=finx_api_endpoint, ssl=True)
surface = finx.calibrate_vol_surface('appendix_b.csv')
print(surface)
```

### Calculation Grid Function Reference

Returns the functions available on the FinX Calculation Grid.

#### list_api_functions()

```python
#! python
import finx
import os
from finx.client import FinXClient

finx_api_key = os.getenv('FINX_API_KEY')
finx_api_endpoint = 'https://hedgefunds.finx.io/api/'
finx = FinXClient('socket', finx_api_key=finx_api_key, finx_api_endpoint=finx_api_endpoint, ssl=True)
functions = finx.list_api_functions()
print(functions)
```
