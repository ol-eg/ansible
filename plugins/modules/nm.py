#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule
import subprocess

DOCUMENTATION = r'''
---
module: nm
short_description: Some network config delivered using GNU Network Manager.
version_added: "0.0.1"
description: |
    Some network config delivered using GNU Network Manager.
    Why not to use command module? Mainly for better idempotency control.
options:
  name:
    description: |
        NM utility which provides the functionality.
        Partially implemented: nmcli.
    default: nmcli
    required: false
    type: str
  object:
    description: |
        Object which NM utility is to operate upon.
        For example if NM utility is nmcli this would be nmcli objects.
        Partially implemented: nmcli objects - networking, wifi
    default: networking
    required: false
  state:
    description: |
        Desired state. Actual value will depend on NM utility and its object.
        name: nmcli, object: networking, state: ['', on, off].
        name: nmcli, object: wifi, state: ['', on, off].
    required: false
    type: str
  connect:
    description: |
        Write me...
    requred: false
    type: dict
author: oleg (@ol-eg)
...
'''
EXAMPLES = r'''
- name: Enable networking control by NM.
  oppa.all.nm:
    name: nmcli
    object: networking
    state: enabled
'''
RETURN = r'''
original_message:
  description: Parameters that were passed in.
  returned: always
  sample: 'name: nmcli, object: networking, state: enabled'
message:
  description: The output message that this module generates.
  type: str
  returned: always
  sample: 'nmcli networking exit code: 0, stdout: enabled'
'''
valid = set([
    (None, None, None),
    ('nmcli', None, None),
    ('nmcli', 'networking', None),
    ('nmcli', 'networking', 'off'),
    ('nmcli', 'networking', 'on'),
    ('nmcli', 'wifi', None),
    ('nmcli', 'wifi', 'off'),
    ('nmcli', 'wifi', 'on'),
])
CMD_TIMEOUT = 180


class nmcli:
    cmd = ['nmcli']
    objects = ('networking', 'wifi')

    def _run_command(self, cmd: list) -> tuple:
        proc = None
        try:
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                universal_newlines=True, bufsize=1,
            )
            out, err = proc.communicate(timeout=CMD_TIMEOUT)
        except OSError as e:
            out, err = ('', str(e))
        except subprocess.TimeoutExpired as e:
            proc.kill()
            out, err = proc.communicate()
            err += str(e)

        return getattr(proc, 'returncode', -9999), out + err

    def _on_off(self, with_args: list, state, result: str):
        # grab current state
        rc, state_before = self._run_command(with_args)
        if rc:
            return True, False, result.format('', rc, 'stderr', state_before)

        if state:
            with_args += [state]

        dontrun = (
            not state,
            state == 'on' and state_before.startswith('enabled'),
            state == 'off' and state_before.startswith('disabled'),
        )
        if any(dontrun):
            return False, False, result.format('', rc, 'stdout', state_before)

        rc, state_after = self._run_command(with_args)
        if rc:
            return True, False, result.format(state, rc, 'stderr', state_after)
        else:
            return (
                False,
                state_before != state_after,
                result.format(state, rc, 'stdout', state_after)
            )

    def networking(self, state=None) -> tuple:
        result = 'nmcli networking {} exit code: {:d}, {}: {}'
        with_args = nmcli.cmd + [nmcli.objects[0]]
        return self._on_off(with_args, state, result)

    def wifi(self, state=None) -> tuple:
        result = 'nmcli radio wifi {} exit code: {:d}, {}: {}'
        with_args = nmcli.cmd + ['radio', nmcli.objects[1]]
        return self._on_off(with_args, state, result)


def validate(module: AnsibleModule, result: dict):
    params = (
        module.params.get('name'),
        module.params.get('object'),
        module.params.get('state')
    )
    if params not in valid:
        result['message'] = 'Invalid parameters choice.'
        module.fail_json(msg='Failed', **result)


def set_defaults(params: dict):
    # this is naive and only works until we implement only nmcli.networking
    keys = ['name', 'object']
    defaults = ['nmcli', 'networking']
    for key, default in zip(keys, defaults):
        if not params.get(key):
            params[key] = default


def run_module():
    module_args = dict(
        name=dict(type='str', required=False),
        object=dict(type='str', required=False),
        state=dict(type='str', required=False),
    )
    result = dict(
        changed=False,
        original_message='',
        message='',
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    if module.check_mode:
        module.exit_json(**result)

    result['original_message'] = f'{module.params}'
    validate(module, result)
    set_defaults(module.params)
    print(module.params['name'])
    util = eval(module.params['name'])()
    func = getattr(util, module.params['object'])
    failed, changed, result['message'] = func(module.params.get('state'))

    if changed:
        result['changed'] = True

    if failed:
        module.fail_json(msg='Failed', **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
