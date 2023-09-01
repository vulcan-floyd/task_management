import json
import os

from pprint import pprint

from werkzeug.exceptions import abort

class TestRequest:
    @classmethod
    def get(self, params):
        client                      = params["client"] if "client" in params else exit("MISSING client")
        url                         = params["url"] if "url" in params else exit("MISSING url")
        expected_status_code        = params["expected_status_code"] if "expected_status_code" in params else 404
        expected_data               = params["expected_data"] if "expected_data" in params else exit("MISSING expected_data")
        query_string                = params["query_string"] if "query_string" in params else None
        
        token = os.environ['TOKEN']
        
        response = client.get(url, query_string=query_string, headers={'x-access-token': token})
        actual_data, actual_status_code = response.data, response.status_code
        actual_data = actual_data.decode('utf-8') if isinstance(actual_data, bytes) else actual_data
        pprint(actual_data)
        print("********************************")
        pprint(expected_data)
        actual_data = json.loads(actual_data)
        assert actual_data == expected_data
        assert actual_status_code == expected_status_code
    
    @classmethod
    def post(self, params):
        client                      = params["client"] if "client" in params else exit("MISSING client")
        url                         = params["url"] if "url" in params else exit("MISSING url")
        data                        = params["data"] if "data" in params else None
        expected_status_code        = params["expected_status_code"] if "expected_status_code" in params else 404
        expected_data               = params["expected_data"] if "expected_data" in params else exit("MISSING expected_data")
        query_string                = params["query_string"] if "query_string" in params else None
        
        token = os.environ['TOKEN']
            
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype,
            'x-access-token': token
        }
        
        response = client.post(url, data=json.dumps(data), headers=headers)
        actual_data, actual_status_code = response.data, response.status_code
        actual_data = json.loads(actual_data.decode('utf-8'))
        pprint(actual_data)
        print("********************************")
        pprint(expected_data)
        assert actual_data == expected_data
        assert actual_status_code == expected_status_code