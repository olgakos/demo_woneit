from utils.base_session import reqres_session

def test_get_good_requiest():
    response = reqres_session().get(url='/company/')
    assert response.status_code == 200

def test_get_bad_request():
    response = reqres_session().get(url='/1217/')
    assert response.status_code == 404