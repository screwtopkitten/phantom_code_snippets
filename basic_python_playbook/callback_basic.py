"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    phantom.debug(container)
    phantom.act(action='geolocate ip',parameters=[{"ip":"182.113.221.215"}],callback=geolocate_ip_cb)
            
    return

def geolocate_ip_cb(action=None,success=None,container=None,results=None,handle=None,filtered_artifacts=None,filtered_results=None,custom_function=None):
    phantom.debug(action)
    phantom.debug(success)
    phantom.debug(container)
    phantom.debug(results)
    phantom.debug(handle)
    phantom.debug(filtered_artifacts)
    phantom.debug(filtered_results)
    phantom.debug(custom_function)
    phantom.act(action='ip reputation',parameters=[{'ip':results[0]["action_results"][0]["parameter"]["ip"]}])
    
    return
    

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    phantom.debug(summary)

    return
