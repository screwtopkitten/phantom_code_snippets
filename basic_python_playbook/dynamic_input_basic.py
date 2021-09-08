"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    name= {"name":"container name"}
    phantom.debug('on_start() called')
    phantom.debug(container)
    param= []
    ips = phantom.collect(container=container, datapath='artifact:*.cef.deviceAddress',scope='all')
    phantom.debug(ips)
    for ip in ips:
        param.append({'ip': ip})
    phantom.debug(param)
    phantom.act(action='geolocate ip',parameters=param,callback=geolocate_ip_cb,handle=name)
            
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
    param= []
    ips = phantom.collect(container=results, datapath='action_result.parameter.ip',scope='all')
    phantom.debug(ips)
    for ip in ips:
        param.append({'ip': ip})
    phantom.act(action='ip reputation',parameters=param)
    
    return
    

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    phantom.debug(summary)

    return
