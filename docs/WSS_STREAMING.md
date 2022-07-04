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

> There is a single endpoint for each stream with all parameters passed in the wss url string. 

### Streaming Ticks

wss://ws.finx.io/streaming/[API Key]/[pair]

The Streaming Ticks service emits a stream of messages that match ticks for the pair provided. 

> The Streaming Ticks service is an aggregation across all available networks. 
> There is no filtering for individual networks at this time - 
> for network-specific time series of ticks (i.e., BINANCE or COINBASE or FTX), use the 
> Tick History function.

#### HOW TO RECEIVE MESSAGES FROM THE STREAMING TICKS SERVICE

1. Connect via wss to wss://[beta or ws].finx.io/streaming/[API Key]/[pair] replacing the variables as appropriate

__*EXAMPLE URL*__
```url
wss://beta.finx.io/streaming/myAPIKey/BTC:USDC
```

2. Once connected, your client will receive messages emitted from the webservice. You must handle these messages in your 
client code.

__*EXAMPLE MESSAGE FROM URL*__

```json
{
  "results": "streaming",
  "resultData": {
    "pair": "BTC:USDC",
    "date": "2022-07-02",
    "time": "15:30:55.817Z",
    "exchange": "BINANCE",
    "price": "19200.84"
  }
}
```

### Streaming Greeks

> Streaming Greeks is scheduled for a future release and is ___not___ available in FinX Python SDK 1.0.0

wss://ws.finx.io/streaming/greeks/[API Key]/[option]

The Streaming Greeks emits a stream of messages that match characteristics of a derivative provided.

> The Streaming Greeks service is an aggregation across all available networks.
> There is no filtering for individual networks at this time -
> for network-specific time series of ticks (i.e., BINANCE or COINBASE or FTX), use the
> Greeks History function [ available in a future release ].

#### HOW TO RECEIVE MESSAGES FROM THE STREAMING GREEKS SERVICE (future release)

1. Connect via wss to wss://[beta or ws].finx.io/streaming/greeks/[API Key]/[option] replacing the variables as 
appropriate, where [option] is formatted as: [underlying_symbol+contract+expiry_year+expiry_month]

__*EXAMPLE URL*__
```url
wss://beta.finx.io/streaming/greeks/myAPIKey/BTCN2202207
```

2. Once connected, your client will receive messages emitted from the webservice. You must handle these messages in your
   client code.

__*EXAMPLE MESSAGE FROM URL*__

```json
{
   "feature": "scheduled for future release"
}
```

