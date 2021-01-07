from collections import namedtuple
from unittest.mock import MagicMock, create_autospec
import pytest
import sys

from .. import nm


class AnsibleModuleMock(MagicMock):
    params = dict(name='nmcli')
    rc = 0
    stdout = 'GENERAL.STATE:100 (connected)'
    stderr = ''

    def exit_json(self, **kwargs):
        sys.exit(0)

    def fail_json(self, **kwargs):
        sys.exit(1)

    def run_command(self, *args, **kwargs):
        if self.rc and kwargs['check_rc']:
            self.fail_json(**kwargs)
        return self.rc, self.stdout, self.stderr


@pytest.fixture(scope='function')
def net_mngr(monkeypatch):
    mock = create_autospec(
        nm.AnsibleModule,
        return_value=AnsibleModuleMock(),
    )
    monkeypatch.setattr(nm, 'AnsibleModule', mock)
    fixture = namedtuple('fixture', 'module mock')
    yield fixture(nm, mock)


def test_run_module(net_mngr):
    with pytest.raises(SystemExit):
        net_mngr.module.run_module()


def test_validate_fails(monkeypatch):
    monkeypatch.setitem(AnsibleModuleMock.params, 'name', 'test')
    result = dict()
    with pytest.raises(SystemExit):
        nm.validate(AnsibleModuleMock(), result)
    assert result['message'] == 'Invalid parameters choice'


def test_invalid_connect(monkeypatch):
    monkeypatch.setitem(
        AnsibleModuleMock.params, 'connect',
        dict(ssid='test', password='test', user='test')
    )
    result = dict()
    with pytest.raises(SystemExit):
        nm.validate(AnsibleModuleMock(), result)
    assert result['message'] == 'Invalid parameters choice'


def test_nmcli_networking_on(monkeypatch):
    monkeypatch.setitem(AnsibleModuleMock.params, 'state', 'on')
    failed, changed, msg = nm.nmcli().networking(AnsibleModuleMock())
    assert not failed
    assert not changed
    assert msg.startswith('nmcli networking on, exit code: 0')


def test_nmcli_wifi_on(monkeypatch):
    monkeypatch.setitem(AnsibleModuleMock.params, 'object', 'wifi')
    monkeypatch.setitem(AnsibleModuleMock.params, 'state', 'on')
    failed, changed, msg = nm.nmcli().wifi(AnsibleModuleMock())
    assert not failed
    assert not changed
    assert msg.startswith('nmcli radio wifi on, exit code: 0')


def test_nmcli_wifi_already_connected(monkeypatch):
    monkeypatch.setitem(AnsibleModuleMock.params, 'object', 'wifi')
    monkeypatch.setitem(
        AnsibleModuleMock.params, 'connect',
        dict(ssid='test', password='test', ifname='test')
    )
    failed, changed, msg = nm.nmcli().wifi(AnsibleModuleMock())
    assert not failed
    assert not changed
    assert 'test already connected' in msg


def test_nmcli_wifi_connect(monkeypatch):
    monkeypatch.setitem(AnsibleModuleMock.params, 'object', 'wifi')
    monkeypatch.setitem(
        AnsibleModuleMock.params, 'connect',
        dict(ssid='test', password='test', ifname='test')
    )
    monkeypatch.setattr(AnsibleModuleMock, 'stdout', 'GENERAL.STATE:30')
    failed, changed, msg = nm.nmcli().wifi(AnsibleModuleMock())
    assert not failed
    assert changed
