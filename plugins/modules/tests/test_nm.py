from unittest.mock import MagicMock, create_autospec
from ansible.module_utils.basic import AnsibleModule

from .. import nm


class AnsibleModuleMock(MagicMock):
    params = dict(name='nmcli', object='networking', state='on')


class NmcliMock(MagicMock):
    def networking(self, state=None):
        return True, True, 'test'


def test_validate_valid():
    module = create_autospec(AnsibleModule)
    for tup in nm.valid:
        d = dict(name=tup[0], object=tup[1], state=tup[2])
        module.params = {k: v for k, v in d.items() if v}
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


def test_nmcli_run_command():
    nmcli = nm.nmcli()
    rc, msg = nmcli._run_command(['echo', 'test'])
    assert not rc
    assert msg == 'test\n'


def test_nmcli_run_command_which_fails():
    nmcli = nm.nmcli()
    rc, msg = nmcli._run_command(['foo'])
    assert rc == -9999
    assert msg == "[Errno 2] No such file or directory: 'foo': 'foo'"


def test_nmcli_run_command_and_timeout(monkeypatch):
    monkeypatch.setattr(nm, 'CMD_TIMEOUT', 1)
    nmcli = nm.nmcli()
    rc, msg = nmcli._run_command(['sleep', '2'])
    assert rc == -9
    assert 'timed out' in msg


def test_on_off_failing_state_before():
    failed, changed, msg = nm.nmcli()._on_off(
        ['ls', '/foo'], None, '{} {:d} {} {}'
    )
    assert failed
    assert not changed
    assert '2 stderr' in msg


def test_on_off_current_state():
    failed, changed, msg = nm.nmcli()._on_off(['ls'], None, '{} {:d} {} {}')
    assert not failed
    assert not changed
    assert '0 stdout' in msg


def test_on_off_against_the_same_state():
    for current, desired in zip(('enabled', 'disabled'), ('on', 'off')):
        failed, changed, msg = nm.nmcli()._on_off(
            ['echo', current], desired, '{} {:d} {} {}'
        )
        assert not failed
        assert not changed
        assert '0 stdout' in msg


def test_on_off_against_opposite_state():
    for current, desired in zip(('enabled', 'disabled'), ('off', 'on')):
        failed, changed, msg = nm.nmcli()._on_off(
            ['echo', current], desired, '{} {:d} {} {}'
        )
        assert not failed
        assert changed
        assert '0 stdout' in msg


def test_on_off_failed_to_change():
    failed, changed, msg = nm.nmcli()._on_off(
        ['ls', '-l'], '/foo', '{} {:d} {} {}'
    )
    assert failed
    assert not changed
    assert '2 stderr' in msg


def test_networking(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(nm.nmcli, '_on_off', mock)
    nm.nmcli().networking('on')
    mock.assert_called_once_with(
        ['nmcli', 'networking'],
        'on',
        'nmcli networking {} exit code: {:d}, {}: {}',
    )


def test_wifi(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(nm.nmcli, '_on_off', mock)
    nm.nmcli().wifi('on')
    mock.assert_called_once_with(
        ['nmcli', 'radio', 'wifi'],
        'on',
        'nmcli radio wifi {} exit code: {:d}, {}: {}',
    )


def test_main(monkeypatch):
    # fall through for syntax and bultins
    monkeypatch.setattr(nm, 'AnsibleModule', AnsibleModuleMock)
    monkeypatch.setattr(nm, 'nmcli', NmcliMock)
    nm.main()
