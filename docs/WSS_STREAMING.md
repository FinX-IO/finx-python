# FinX Websocket Service

## WSS: Streaming

#### The FinX Streaming service is a websocket server that can be used in 2 ways:

1. STREAMS: Listen for messages on a streaming channel (live streaming)
2. FUNCTIONS: Make function calls over a websocket connection (faster throughput and lower overhead)

## Endpoints

> ##### WSS Production Base Endpoint: 
> wss://ws.finx.io/

> ##### WSS Beta Endpoint: 
> wss://beta.finx.io/

***

## STREAMS

### HOW TO CONNECT
> There is a single endpoint used to call any streaming function. Once connected, send a message into the websocket connection
> which contains the inputs for that function. You must always include your APIKey in messages you submit to the websocket server. 

1. First, establish a websocket connection to one of the following endpoints:

    - wss://ws.finx.io/streamer/[API Key]

    - wss://beta.finx.io/streamer/[API Key]

2. Once connected, you may submit messages over that connection to the endpoints and receive responses.
3. If you intend to keep your socket open and stream messages for longer than 5 minutes, you must submit
 a "keepAlive" message to the server (an interval of 270 seconds will keep the channel open).

### Streaming Data and Functions

You may subscribe to a stream by submitting a message to the server after connecting over websocket.

#### functionName: keepAlive

The Streaming data service can be kept alive by submitting a keepAlive message every 4 minutes and 30 seconds. 

#### MESSAGE FORMAT FOR KEEP ALIVE

```json
{
  "APIKey": {your finx api key},
  "functionName": "keepAlive"
}
```

##### RESPONSE

```json
{
  "keepAlive": true
}
```

#### functionName: listDeribitContracts

The Streaming Contracts service has a list of all contracts available.

#### MESSAGE FORMAT FOR LIST DERIBIT CONTRACTS

```json
{
  "APIKey": {your finx api key},
  "functionName": "listDeribitContracts"
}
```

##### RESPONSE

```json
["BTC-8AUG22-18000-C", "BTC-8AUG22-18000-P", "BTC-8AUG22-19000-C", "BTC-8AUG22-19000-P", "BTC-8AUG22-20000-C", "BTC-8AUG22-20000-P", "BTC-8AUG22-21000-C", "BTC-8AUG22-21000-P", ...]
```


#### functionName: getDeribitContractStream

The Streaming Contracts service emits a stream of messages that match contract ticker data for the contract submitted (instrumentName). 

Streaming Contracts include risk measures and price information real-time for a contract.

#### MESSAGE FORMAT FOR SUBSCRIBING TO STREAMING CONTRACTS

```json
{
  "APIKey": {your finx api key},
  "functionName": "getDeribitContractStream",
  "instrumentName": {format is like BTC-26AUG22-20000-C}
}
```

##### RESPONSE

```json
{
  "redis_key": "BTC-26AUG22-20000-C",
  "underlying_price": "23227.53",
  "underlying_index": "BTC-26AUG22",
  "timestamp": "1659760300724",
  "state": "open",
  "settlement_price": "0.15522931",
  "open_interest": "846.5",
  "min_price": "0.1205",
  "max_price": "0.197",
  "mark_price": "0.1553",
  "mark_iv": "72.12",
  "last_price": "0.1535",
  "interest_rate": "0",
  "instrument_name": "BTC-26AUG22-20000-C",
  "index_price": "23199.76",
  "estimated_delivery_price": "23199.76",
  "bid_iv": "0",
  "best_bid_price": "0.125",
  "best_bid_amount": "5",
  "best_ask_price": "0.19",
  "best_ask_amount": "5",
  "ask_iv": "122.66",
  "vega": "13.62974",
  "theta": "-24.39797",
  "rho": "8.69414",
  "gamma": "0.00006",
  "delta": "0.83341",
  "volume": "3.3",
  "price_change": "-3.2258",
  "low": "0.15",
  "high": "0.162"
}
```

You may use a single connection to subscribe to multiple streams at once.

#### functionName: listDeribitContracts

#### Message Format

```json
{
  "APIKey": {your finx api key},
  "functionName": "listDeribitContracts"
}
```

#### RESPONSE MESSAGE

EXAMPLE ONLY THIS IS NOT A COMPLETE LIST

```array
["BTC-6AUG22-18000-C", "BTC-6AUG22-18000-P", "BTC-6AUG22-19000-C", "BTC-6AUG22-19000-P", "BTC-6AUG22-20000-C", "BTC-6AUG22-20000-P", "BTC-6AUG22-21000-C", "BTC-6AUG22-21000-P", "BTC-6AUG22-21500-C", "BTC-6AUG22-21500-P", "BTC-6AUG22-22000-C", "BTC-6AUG22-22000-P", "BTC-6AUG22-22500-C", "BTC-6AUG22-22500-P", "BTC-6AUG22-23000-C", "BTC-6AUG22-23000-P", "BTC-6AUG22-23500-C", "BTC-6AUG22-23500-P", "BTC-6AUG22-24000-C", "BTC-6AUG22-24000-P", "BTC-6AUG22-25000-C", "BTC-6AUG22-25000-P", "BTC-6AUG22-26000-C", "BTC-6AUG22-26000-P", "BTC-7AUG22-18000-C", "BTC-7AUG22-18000-P", "BTC-7AUG22-19000-C", "BTC-7AUG22-19000-P", "BTC-7AUG22-20000-C",... "ETH-12AUG22-1250-C", "ETH-12AUG22-1250-P", "ETH-12AUG22-1300-C", "ETH-12AUG22-1300-P", "ETH-12AUG22-1350-C", "ETH-12AUG22-1350-P", "ETH-12AUG22-1400-C", "ETH-12AUG22-1400-P", "ETH-12AUG22-1450-C", "ETH-12AUG22-1450-P", "ETH-12AUG22-1500-C", "ETH-12AUG22-1500-P", "ETH-12AUG22-1550-C", "ETH-12AUG22-1550-P", "ETH-12AUG22-1600-C", "ETH-12AUG22-1600-P", "ETH-12AUG22-1650-C", "ETH-12AUG22-1650-P", "ETH-12AUG22-1700-C", "ETH-12AUG22-1700-P", "ETH-12AUG22-1750-C", "ETH-12AUG22-1750-P", "ETH-12AUG22-1800-C", "ETH-12AUG22-1800-P", "ETH-12AUG22-1850-C", "ETH-12AUG22-1850-P", "ETH-12AUG22-1900-C", "ETH-12AUG22-1900-P", "ETH-12AUG22-2000-C", "ETH-12AUG22-2000-P", "ETH-12AUG22-2100-C", "ETH-12AUG22-2100-P", "ETH-12AUG22-2200-C", "ETH-12AUG22-2200-P", "ETH-12AUG22-2400-C", "ETH-12AUG22-2400-P", "ETH-12AUG22-2600-C", "ETH-12AUG22-2600-P", "ETH-12AUG22-2800-C", "ETH-12AUG22-2800-P", "ETH-12AUG22-3000-C", "ETH-12AUG22-3000-P", "ETH-19AUG22", "ETH-19AUG22-800-C", "ETH-19AUG22-800-P", "ETH-19AUG22-1000-C", "ETH-19AUG22-1000-P", "ETH-19AUG22-1100-C", "ETH-19AUG22-1100-P", "ETH-19AUG22-1200-C", "ETH-19AUG22-1200-P", "ETH-19AUG22-1300-C", "ETH-19AUG22-1300-P", "ETH-19AUG22-1350-C", "ETH-19AUG22-1350-P", "ETH-19AUG22-1400-C", "ETH-19AUG22-1400-P", "ETH-19AUG22-1450-C", "ETH-19AUG22-1450-P", "ETH-19AUG22-1500-C", "ETH-19AUG22-1500-P", "ETH-19AUG22-1550-C",... "SOL-12AUG22-26-P", "SOL-12AUG22-28-C", "SOL-12AUG22-28-P", "SOL-12AUG22-30-C", "SOL-12AUG22-30-P", "SOL-12AUG22-31-C", "SOL-12AUG22-31-P", "SOL-12AUG22-32-C", "SOL-12AUG22-32-P", "SOL-12AUG22-33-C", "SOL-12AUG22-33-P", "SOL-12AUG22-34-C", "SOL-12AUG22-34-P", "SOL-12AUG22-35-C", "SOL-12AUG22-35-P", "SOL-12AUG22-36-C", "SOL-12AUG22-36-P", "SOL-12AUG22-37-C", "SOL-12AUG22-37-P", "SOL-12AUG22-38-C", "SOL-12AUG22-38-P", "SOL-12AUG22-39-C", "SOL-12AUG22-39-P", "SOL-12AUG22-40-C", "SOL-12AUG22-40-P", "SOL-12AUG22-41-C", "SOL-12AUG22-41-P", "SOL-12AUG22-42-C", "SOL-12AUG22-42-P", "SOL-12AUG22-43-C", "SOL-12AUG22-43-P", "SOL-12AUG22-44-C", "SOL-12AUG22-44-P", "SOL-12AUG22-45-C", "SOL-12AUG22-45-P", "SOL-12AUG22-46-C", "SOL-12AUG22-46-P", "SOL-12AUG22-47-C", "SOL-12AUG22-47-P", "SOL-12AUG22-48-C", "SOL-12AUG22-48-P", "SOL-12AUG22-49-C", "SOL-12AUG22-49-P", "SOL-12AUG22-50-C", "SOL-12AUG22-50-P", "SOL-12AUG22-51-C", "SOL-12AUG22-51-P", "SOL-12AUG22-52-C", "SOL-12AUG22-52-P", "SOL-12AUG22-54-C", "SOL-12AUG22-54-P", "SOL-12AUG22-55-C", "SOL-12AUG22-55-P", ..."SOL-PERPETUAL", "AVAX_USDC-PERPETUAL", "MATIC_USDC-PERPETUAL", "ETH_USDC-PERPETUAL", "BCH_USDC-PERPETUAL", "ADA_USDC-PERPETUAL", "LINK_USDC-PERPETUAL", "DOT_USDC-PERPETUAL", "BTC_USDC-PERPETUAL", "TRX_USDC-PERPETUAL", "ALGO_USDC-PERPETUAL", "DOGE_USDC-PERPETUAL", "NEAR_USDC-PERPETUAL", "LTC_USDC-PERPETUAL", "XRP_USDC-PERPETUAL", "SOL_USDC-PERPETUAL", "UNI_USDC-PERPETUAL"]
```


### Streaming Spot rates

> The Streaming Ticks service is an aggregation across all available networks. 
> There is no filtering for individual networks at this time - 
> for network-specific time series of ticks (i.e., BINANCE or COINBASE or FTX), use the 
> Tick History function.

#### MESSAGE FORMAT FOR SUBSCRIBING TO STREAMING SPOT RATES

```json
{
  "APIKey": {your finx api key},
  "functionName": "getSpotRates",
  "pair": {format is like BTC:USDC}
}
```

### RESPONSE MESSAGE 

```json
{
  "pair": "BTC:USDC",
  "unixDate": 1659897295,
  "UTCDate": "2022-08-07T18:34:55.000Z",
  "exchange": "BINANCE",
  "price": "23233.684999999998"
}
```
