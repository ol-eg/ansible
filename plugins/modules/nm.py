#!/usr/bin/python3

DOCUMENTATION = r'''
---
module: nm
short_description: Some network config delivered using GNU Network Manager.
version_added: "0.0.1"
description: Some network config delivered using GNU Network Manager.
options:
  name:
    description: >
        NM utility which provides the functionality.
        Partially implemented: nmcli.
    default: nmcli
    required: false
    type: str
  object:
    description: >
        Object which NM utility is to operate upon.
        For example if NM utility is nmcli this would be nmcli objects.
        Partially implemented: nmcli objects - networking
    default: networking
    required: false
  state:
    description: >
        Desired state. Actual value will depend on the NM utility and its object.
        Not implemented.
    required: false
    type: str
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
  sample: "{name: nmcli, object: networking, state: enabled}"
message:
  description: The output message that this module generates.
  type: str
  returned: always
  sample: 'nmcli.networking = enabled'
'''
from ansible.module_utils.basic import AnsibleModule

valid = set([
    (None, None, None),
    ('nmcli', None, None),
    ('nmcli', 'networking', None),
    ('nmcli', 'networking', 'off'),
    ('nmcli', 'networking', 'on'),
])


def validate(module: AnsibleModule, result: dict):
    params = (
        module.params.get('name'),
        module.params.get('object'),
        module.params.get('state')
    )
    if params not in valid:
        result['message'] =  'Invalid parameters choice.'
        module.fail_json(msg='Failed', **result)


def set_defaults(params: dict):
    # this is naive and only works until we implement only nmcli.networking
    keys = ['name', 'object']
    defaults = ['nmcli', 'networking']
    for key, default in zip(keys, defaults):
        if not params.get(key):
            params[key] = default


class nmcli:
    def networking(self, state: str):
        return  True, True, 'All good'


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
    print(module.params)
    util = eval(module.params['name'])()
    func = getattr(util, module.params.get('object', 'networking'))
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
