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
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return
