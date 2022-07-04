# FinX Python Functions

#### The FinX Streaming service is a websocket server that can be used in 2 ways:

1. STREAMS: Listen for messages on a streaming channel (live streaming)
2. FUNCTIONS: Make function calls over a websocket connection (faster throughput and lower overhead)

## Endpoints

> ##### WSS Production Base Endpoint: 
> wss://ws.finx.io/

> ##### WSS Beta Endpoint: 
> wss://beta.finx.io/

## FINX WSS FUNCTIONS

### Authenticate

wss://ws.finx.io/backend/[params]

#### HOW TO RECEIVE MESSAGES FROM THE AUTHENTICATION SERVICE

1. Connect via wss to wss://[beta or ws].finx.io/backend/[params] where params contains APIKey

__*EXAMPLE URL*__
```url
wss://beta.finx.io/backend/[params]
```

2. Once connected, your client will receive a message containing Authentication Response in a single json object emitted from the
   webservice. You must handle this message in your client code.

```json
{"isAuth": true}
```

### Tick Snap

wss://ws.finx.io/backend/[params]

#### HOW TO RECEIVE MESSAGES FROM THE TICK SNAP SERVICE

1. Connect via wss to wss://[beta or ws].finx.io/backend/[params] where params contains APIKey, pair, date, time

__*EXAMPLE URL*__
```url
wss://beta.finx.io/backend/[params]
```

2. Once connected, your client will receive a message containing the tick snap in a single json object emitted from the
   webservice. You must handle this message in your client code.

```json
{
    "pair":"BTC:USD",
    "date":"2022-06-15",
    "time":"21:27:40.453Z",
    "exchange":"COINBASE",
    "price":"21865.010000000002"
}
```

### Tick History

This method currently returns 1000 rows at a time for a specific day. You must specify a single pair and the date. The "date" entered
is the *DAY* for the historical return series. If a "time" is entered, results will be for the *DAY* entered and _after_ the *TIME* entered. 
Items are not sorted by time, you will have to order the
result set when you receive it.

In a future release, we will include the following parameters:

- number of observations (future, up to a max of 1000)
- frequency of ticks across time window (future)
- my_date is starting time (0.0.2 included)
- my_end_date is ending window (future)

wss://ws.finx.io/backend/[params]

#### HOW TO RECEIVE MESSAGES FROM THE TICK HISTORY SERVICE

1. Connect via wss to wss://[beta or ws].finx.io/backend/[params] where params contains APIKey, pair, date, time

__*EXAMPLE URL*__
```url
wss://beta.finx.io/backend/[params]
```

2. Once connected, your client will receive a message containing the history in a single json object emitted from the 
webservice. You must handle this message in your client code.

__*EXAMPLE MESSAGE FROM URL*__

```json
{
    "0":{
        "pair":"BTC:USD",
        "date":"2022-06-15",
        "time":"21:27:40.453Z",
        "exchange":"COINBASE",
        "price":"21865.010000000002"},
    "1":{
        "pair":"BTC:USD","date":"2022-06-15",
        "time":"18:07:17.110Z",
        "exchange":"COINBASE",
        "price":"20871.54"},
    "2":{
        "pair":"BTC:USD",
        "date":"2022-06-15",
        "time":"11:57:01.842Z",
        "exchange":"GEMINI",
        "price":"21100.50"},
    "3":{
        "pair":"BTC:USD",
        "date":"2022-06-15",
        "time":"08:47:43.619Z",
        "exchange":"FTX",
        "price":"20209.32"},#...
}
```

#### Calculate Greeks

[ this feature is scheduled for a future release ]

```json
my_contract = 'BTC2WMF'
my_option_price = '100'
my_strike_price = '30000'
my_days_to_expiry = '5'
greeks = await my_tick_client.calculate_greeks(my_pair, my_cadence)
```

### Reference Data

[ this feature is scheduled for a future release ]

### Ratings Data

[ this feature is scheduled for a future release ]

### HTTPS

#### HTTPS REST: Functions

[ this feature is scheduled for a future release ]

### Other

[ this feature is scheduled for a future release ]

#### TCP Socket

[ this feature is scheduled for a future release ]