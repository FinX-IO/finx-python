# FinX Python SDK

## Python Reference

1. Tick Streamer
2. Tick Snap
3. Tick History

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
tick_history = tick_plant.tick_history("BTC:USDC","2022-06-01","00:00")
print(tick_history)
```
