"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    name= {"name":"container name"}
    phantom.debug('on_start() called')
    phantom.debug(container)
            
    return
    

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    phantom.debug(summary)

    return
