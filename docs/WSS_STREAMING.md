# FinX Python Streamer

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

> There is a single endpoint used to call any streaming function. Once connected, send a message into the websocket connection
> which contains the inputs for that function. You must always include your APIKey in messages you submit to the websocket server. 

wss://ws.finx.io/streaming/[API Key]
wss://beta.finx.io/streaming/[API Key]

### Streaming Contracts

The Streaming Contracts service emits a stream of messages that match contract ticker data for the contract submitted (instrumentName). 

Streaming Contracts include risk measures and price information real-time for a contract.

You may subscribe to a stream by submitting a message to the server.

#### MESSAGE FORMAT FOR SUBSCRIBING TO STERAMING CONTRACTS

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
