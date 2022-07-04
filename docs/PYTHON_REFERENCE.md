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

streamer = Streamer(dict(pair='BTC:USDC'))
streamer.connect()
streamer.listen('output.txt')
```

