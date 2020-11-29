from .. import nm

def test_set_defaults():
    params = dict()
    nm.set_defaults(params)
    assert params == dict(name='nmcli', object='networking')
