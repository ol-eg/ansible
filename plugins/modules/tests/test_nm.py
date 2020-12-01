from unittest.mock import MagicMock, create_autospec
from ansible.module_utils.basic import AnsibleModule
import pytest

from .. import nm


def test_validate_valid():
    module = create_autospec(AnsibleModule)
    for tup in nm.valid:
        d = dict(name=tup[0], object=tup[1], state=tup[2])
        module.params = {k:v for k,v in d.items() if v}
        nm.validate(module, dict())
        module.fail_json.assert_not_called()

def test_validate_invalid():
    module = create_autospec(AnsibleModule)
    module.params = dict(name='foobar')
    nm.validate(module, dict())
    module.fail_json.assert_called_with(
        message='Invalid parameters choice.', msg='Failed'
    )


def test_set_defaults():
    params = dict()
    nm.set_defaults(params)
    assert params == dict(name='nmcli', object='networking')


def test_main(monkeypatch):
    class AnsibleModuleMock(MagicMock):
        params = dict()

    monkeypatch.setattr(nm, 'AnsibleModule', AnsibleModuleMock())
    nm.main()
