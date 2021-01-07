#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule  # type: ignore
from typing import Dict, List, Tuple, Union

DOCUMENTATION = r'''
---
module: nm
short_description: Network config using GNU Network Manager.
version_added: "0.0.1"
description: Network config using GNU Network Manager.
options:
    name:
        description: |
            NM utility name.
            Partially implemented -- nmcli.
        required: true
        type: str
    object:
        description: |
            Object which NM utility is to operate upon.
            e.g. NM utility 'nmcli' objects: 'networking', 'wifi'.
            Partially implemented -- nmcli objects:
            networking, wifi.
        default: networking (if name is nmcli)
        required: false
        type: str
    state:
        description: |
            Desired state. Context dependant. Implemented --
            name: nmcli, object: networking, state: [None, on, off]
            name: nmcli, object: wifi, state: [None, on, off]
        requred: false
        type: str
    connect:
        description: |
            Create new connection and activate it on a wifi device.
            It is assumed that IP config is via dhcp.
            Keys: ssid, password, ifname.
            Only wifi connect is implemented.
        required: false
        type: dict
author: oleg (@ol-eg)
...
'''  # type: str
EXAMPLES = r'''
---
- hosts: localhost
  become: yes
  vars_prompt:
    - name: password
      prompt: wifi password?
  tasks:
    - name: Enable networking control by NM.
      oppa.all.nm:
        name: nmcli
        object: networking
        state: "on"
    - name: Enable wifi.
      oppa.all.nm:
        name: nmcli
        object: wifi
        state: "on"
    - name: Connect to wifi network.
      oppa.all.nm:
        name: nmcli
        object: wifi
        connect:
          ssid: Tinco116_5G
          password: '{{ password }}'
          ifname: wlp58s0
      no_log: true
...
'''  # type: str
RETURN = r'''
---
original_message:
    description: Parameters that were passed in.
    type: str
    returned: always
    sample: "'{''name'': ''nmcli'', ''object'': ''networking''}"
message:
    description: The module's output message.
    type: str
    returned: always
    sample: 'nmcli networking, exit code: 0, stdout: enabled'
...
'''  # type: str

Result = Dict[str, Union[str, bool]]
Utils = Union['nmcli', ]

VALID = set([
    ('nmcli', None),
    ('nmcli', None, None),
    ('nmcli', 'networking', None),
    ('nmcli', 'networking', 'off'),
    ('nmcli', 'networking', 'on'),
    ('nmcli', 'wifi', None),
    ('nmcli', 'wifi', 'off'),
    ('nmcli', 'wifi', 'on'),
])


class nmcli:
    def _on_off(
        self, args: List[str], result: str, module: AnsibleModule,
    ) -> Tuple[bool, bool, str]:
        # grab current state
        rc, state_before, stderr = module.run_command(
            args, check_rc=True,
        )
        state = module.params.get('state')
        donotrun = (
            not state,
            state == 'on' and state_before.startswith('enabled'),
            state == 'off' and state_before.startswith('disabled'),
        )
        if any(donotrun):
            return (
                False, False,
                result.format('', rc, 'stdout', state_before)
            )
        rc, state_after, stderr = module.run_command(
                args + [state], check_rc=True,
        )
        return (
            False, state_before != state_after,
            result.format(state, rc, 'stdout', state_after),
        )

    def networking(
            self, module: AnsibleModule
    ) -> Tuple[bool, bool, str]:
        result = 'nmcli networking {}, exit code: {:d}, {}: {}'
        return self._on_off(
            ['nmcli', 'networking'], result, module,
        )

    def wifi(self, module: AnsibleModule) -> Tuple[bool, bool, str]:
        result = 'nmcli radio wifi {}, exit code: {:d}, {}: {}'
        if module.params.get('state'):
            return self._on_off(
                ['nmcli', 'radio', 'wifi'], result, module,
            )
        elif module.params.get('connect'):
            return self.wifi_connect(result, module)
        else:
            return True, False, result.format(
                '', -1000, 'stderr', 'Not implemented wifi command')

    def wifi_connect(
        self, result: str, module: AnsibleModule
    ) -> Tuple[bool, bool, str]:
        conn = module.params.get('connect')
        # let's see if wifi is connected
        rc, stdout, stderr = module.run_command(
            ['nmcli', '-t', 'device', 'show', conn['ifname']],
            check_rc=True
        )
        state = [
            s for s in stdout.split('\n') if s.startswith('GENERAL.STATE')
        ][0].split(':')[-1]
        if state.startswith('100'):
            return False, False, result.format(
                'connect', rc,
                'stdout', f'{conn["ifname"]} already connected')
        # let's try to connect
        args = [
            'nmcli', '-t', 'device', 'wifi', 'connect',
            conn['ssid'], 'password', conn['password'],
            'ifname', conn['ifname'],
        ]
        rc, stdout, stderr = module.run_command(args, check_rc=True)
        return False, True, result.format('connect', rc, 'stdout', stdout)


def validate(module: AnsibleModule, result: Result) -> None:
    params = (
        module.params.get('name'),
        module.params.get('object'),
        module.params.get('state'),
    )
    if params not in VALID or not validate_connect(module):
        result['message'] = 'Invalid parameters choice'
        module.fail_json(msg='Failed', **result)


def validate_connect(module: AnsibleModule) -> bool:
    if module.params.get('connect'):
        keys = module.params['connect'].keys()
        for key in ('ssid', 'password', 'ifname'):
            if key not in keys:
                return False
    return True


def set_defaults(params: Dict[str, str]) -> None:
    if params['name'] == 'nmcli':
        if not params.get('object'):
            params['object'] = 'networking'


def run_module() -> None:
    module_args = dict(
        name=dict(type='str', required=True),
        object=dict(type='str', required=False),
        state=dict(type='str', required=False),
        connect=dict(type=dict, required=False)
    )
    module = AnsibleModule(argument_spec=module_args)
    result: Result = dict(
        changed=False, original_message='', message=''
    )
    result['original_message'] = f'{module.params}'
    validate(module, result)
    set_defaults(module.params)
    util: Utils = eval(module.params['name'])()
    f = getattr(util, module.params['object'])
    failed, result['changed'], result['message'] = f(module)
    if failed:
        module.fail_json(msg='Failed', **result)
    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
