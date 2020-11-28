from interfaces.jfrog_api import JfrogAPI
from configs import endpoints
import json


def get_health_ping(client: JfrogAPI) -> str:
    try:
        endpoint = endpoints.HEALTH_PING
        res = client.request(endpoint['method'].value, endpoint['url'])
        if res['success']:
            if res['ok']:
                return "Artifactory is Alive !"
            else:
                return "Artifactory might be Down - " + str(res['response'].status_code) + " - " + res['message']
        else:
            return "Artifactory might be Down - " + res['error']

    except Exception as e:
        return "Artifactory might be Down - Unknown exception"


def get_system_version(client: JfrogAPI) -> str:
    try:
        endpoint = endpoints.SYSTEM_VERSION
        res = client.request(endpoint['method'].value, endpoint['url'])
        if res['success']:
            if res['ok']:
                response_json = json.loads(res['response'].content)
                if "version" in response_json.keys():
                    return "Artifactory Version: " + response_json['version']
                else:
                    return "Error finding version : No version"
            else:
                return "Error finding version : " + str(res['response'].status_code) + " - " + res['message']
        else:
            return "Error finding version" + res['error']

    except Exception as e:
        return "Error - Unknown exception"


def user_handling_by_name(client: JfrogAPI, username: str, email: str, password: str,
                          is_deletion: bool = False) -> str:
    try:
        if is_deletion:
            endpoint = endpoints.DELETE_USER
        else:
            endpoint = endpoints.CREATE_USER
        data = {"email": email, "password": password}
        res = client.request(endpoint['method'].value, endpoint['url'].format(username), data)
        if res['success']:
            if res['ok']:
                if is_deletion:
                    return "Deleted successfully !"
                else:
                    return "Created successfully !"
            else:
                return "Error creating user : " + str(res['response'].status_code) + " - " + res['message']
        else:
            return "Error creating user: " + res['error']

    except Exception as e:
        return "Error creating user: unknown exception"


def get_storage_info(client: JfrogAPI) -> str:
    try:
        endpoint = endpoints.STORAGE_INFO
        res = client.request(endpoint['method'].value, endpoint['url'])
        if res['success']:
            if res['ok']:
                storage_info_json = json.loads(res['response'].content)
                return json.dumps(storage_info_json, indent=1, sort_keys=True)
            else:
                return "Error retrieving storage info - " + str(res['response'].status_code) + " - " + res['message']
        else:
            return "Error retrieving storage info - " + res['error']

    except Exception as e:
        return "Error retrieving storage info - unknown exception"
