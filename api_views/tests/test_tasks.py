from api_views.tests.test_utils.TestRequest import TestRequest

BASE_URL = "/task"
SUCCESS_STATUS_CODE = 200
NOT_FOUND_STATUS_CODE = 404


def test_taskViewId(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/3/tasks",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "expected_data"         :   {"tasks": {"description": "Algebra Homework.",
                                               "due_date": "Fri, 01 Sep 2023 10:45:07 GMT",
                                               "id": 3,
                                               "status": "NotPicked",
                                               "title": "Algebra",
                                               "priority": "Low",
                                               }
                                    }
    }
    TestRequest.get(params)
    
def test_taskView(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/tasks",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "expected_data"         :   {"tasks": [{"description": "Science Homework",
                                                "due_date": "Fri, 01 Sep 2023 10:45:07 GMT",
                                                "id": 1,
                                                "status": "InProgress",
                                                "title": "Science",
                                                "priority": "Low",
                                                },
                                                {"description": "Math Homework.",
                                                 "due_date": "Fri, 01 Sep 2023 10:45:07 GMT",
                                                 "id": 2,
                                                 "status": "InProgress",
                                                 "title": "Math",
                                                 "priority": "Medium",}]
                                    }
    }
    TestRequest.get(params)
    
def test_taskViewId_Not_Task(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/9/tasks",
        "expected_status_code"  :   NOT_FOUND_STATUS_CODE,
        "expected_data"         :   {"error": 404, "text": "No Task found for given Id"}
    }
    TestRequest.get(params)
    
def test_taskFilterView(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/filter/tasks",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "query_string"          :   {'status': 'InProgress'},
        "expected_data"         :   {"tasks": [{"id": 1,
                                                "status": "InProgress",
                                                "title": "Science",
                                                "priority": "Low"
                                                },
                                                {"id": 2,
                                                 "status": "InProgress",
                                                 "title": "Math",
                                                 "priority": "Medium"}]
                                    }
    }
    TestRequest.get(params)
    
def test_taskFilterView_NotFoundTask(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/filter/tasks",
        "expected_status_code"  :   NOT_FOUND_STATUS_CODE,
        "query_string"          :   {'status': 'Completed'},
        "expected_data"         :   {"error": 404, "text": "No Task found for given Filter"}
    }
    TestRequest.get(params)
    
def test_createTask(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/create",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "data"                  :   {"title": "Dummy",
                                     "description": "Create Dummy Task for the project",
                                     "due_date": "2023-09-4",
                                     "priority": "low"},
        "expected_data"         :   {"data": 'Dummy'},
    }
    TestRequest.post(params)
    
def test_taskSortedView_ByTitle(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/sort/tasks",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "query_string"          :   {'sort_by': 'title'},
        "expected_data"         :   {"tasks": [{"id": 3,
                                               "status": "NotPicked",
                                               "title": "Algebra",
                                               "priority": "Low"
                                               },
                                                {"id": 4,
                                                 "status": "NotPicked",
                                                 "title": "Calculus",
                                                 "priority": "High"
                                                }]
                                    }
    }
    TestRequest.get(params)
   
def test_taskSortedView_ById(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/sort/tasks",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "query_string"          :   {'sort_by': 'id'},
        "expected_data"         :   {"tasks": [{"id": 1,
                                               "status": "InProgress",
                                               "title": "Science",
                                               "priority": "Low"
                                               },
                                                {"id": 2,
                                                 "status": "InProgress",
                                                 "title": "Math",
                                                 "priority": "Medium"
                                                }]
                                    }
    }
    TestRequest.get(params)
    
def test_taskFilterPriorityView(test_client):
    params = {
        "client"                :   test_client,
        "url"                   :   f"{BASE_URL}/filter/priority/tasks",
        "expected_status_code"  :   SUCCESS_STATUS_CODE,
        "expected_data"         :   {"tasks": [{"id": 1,
                                               "status": "InProgress",
                                               "title": "Science",
                                               "priority": "Low"
                                               },
                                                {"id": 3,
                                                 "status": "NotPicked",
                                                 "title": "Algebra",
                                                 "priority": "Low"
                                                }]
                                    }
    }
    TestRequest.get(params)
    