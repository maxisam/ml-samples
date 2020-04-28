import requests
import json
import datetime
import os

# Imports the Google Cloud client library
import google.cloud.logging
import logging

def _set_logging_client():
    # Instantiates a client
    client = google.cloud.logging.Client()

    # Connects the logger to the root logging handler; by default this captures
    # all logs at INFO level and higher
    client.setup_logging()

def _get_payload():
    payload = {
        "instances": 
            [
                {
                    "8496745483987845120":1,
                    "282179763664060416":1,
                    "2155677208650186752":1,
                    "5614441722470727680":1,
                    "9073206236291268608":1,
                    "7920284731684421632":1,
                    "4461520217863880704":1,
                    "714525327891628032":1,
                    "2443907584801898496":1,
                    "1290986080195051520":1,
                    "7055593603229286400":1,
                    "3596829089408745472":1,
                    "5902672098622439424":1,
                    "8208515107836133376":1,
                    "5326211346319015936":1,
                    "3020368337105321984":1,
                    "7632054355532709888":1,
                    "1867446832498475008":1,
                    "8784975860139556864":1,
                    "4173289841712168960":1,
                    "6479132850925862912":1,
                    "2732137960953610240":1,
                    "426294951739916288":1,
                    "5037980970167304192":1,
                    "7343823979380998144":1,
                    "1579216456346763264":1,
                    "3885059465560457216":1,
                    "6190902474774151168":1,
                    "1002755704043339776":1,
                    "3308598713257033728":1
                }
            ]
    }

    return json.dumps(payload)

url = os.getenv('URL')

payload = _get_payload()
_set_logging_client()

while True:
    time_now = datetime.datetime.now()
    result = requests.post(url=url, data=payload)
    total_time = datetime.datetime.now() - time_now

    logging.warning(str(total_time.microseconds/1000))
    logging.warning(result.text)