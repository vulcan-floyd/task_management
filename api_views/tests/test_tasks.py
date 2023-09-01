from api_views.tests.test_utils.TestRequest import TestRequest

BASE_URL = "/task"

def test_taskViewId(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/3/tasks",
        # "expected_status_code"  :   NOT_FOUND_STATUS_CODE,
        "query_string"          :   {'exclude_tags': '46733'},
        # "ignore_keys"           :   ["data.posts.0.user_reaction", "data.posts.0.reaction_count"],
        "expected_data"         :   {"tasks": {
                                                "id": 3,
                                                "title": "Algebra",
                                                "description": "Algebra Homework.",
                                                # "status": "NotPicked",
                                                "due_date": "Fri, 01 Sep 2023 10:45:07 GMT"
                                                }
                                    }
    }
    TestRequest.test_get(params)
    
def test_taskView(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/tasks",
        "query_string"          :   {'exclude_tags': '46733'},
        "expected_data"         :   {"tasks": [{"id": 1,
                                                "title": "Science"},
                                               {"id": 2,
                                                "title": "Math"},]
                                    }
    }
    TestRequest.test_get(params)