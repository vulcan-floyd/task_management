import json
import os

from pprint import pprint

from werkzeug.exceptions import abort

class TestRequest:
    @classmethod
    def test_get(self, params, header_token=''):
        client                      = params["client"] if "client" in params else exit("MISSING client")
        url                         = params["url"] if "url" in params else exit("MISSING url")
        expected_data               = params["expected_data"] if "expected_data" in params else exit("MISSING expected_data")
        query_string                = params["query_string"] if "query_string" in params else None
        
        if header_token:
            token = header_token
        else:
            token = os.environ['TOKEN']
        
        response = client.get(url, query_string=query_string, headers={'x-access-token': token})
        actual_data = response.data
        actual_data = actual_data.decode('utf-8') if isinstance(actual_data, bytes) else actual_data
        pprint(actual_data)
        print("********************************")
        pprint(expected_data)
        actual_data = json.loads(actual_data)
        assert actual_data == expected_data
        # assert actual_status_code == expected_status_code