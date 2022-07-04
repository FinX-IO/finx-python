#! python
#  This test script requires a FinX API Key
#  For information on this test script, email info@finx.io
import os

from finx.finx_streamer import Streamer

def main_synchronous(environment: str = "dev"):
    streamer = Streamer(dict(api_key=os.getenv('FINX_API_KEY'),pair="BTC:USD"), environment)
    connect_data: dict = streamer.connect()
    print(f'**********************\nBTC:USD SNAP DATA: {connect_data}\n\n')


if __name__ == '__main__':
    print('-----> FinX Test Runner ----->')
    print(' ')
    finx_api_key = input("Please enter your FinX API Key --> ")
    os.environ['FINX_API_KEY'] = finx_api_key
    """
    There are 2 ways to use the sdk client
    (1) Synchronous
    (2) Async
    """
    # RUN SYNC
    main_synchronous()
