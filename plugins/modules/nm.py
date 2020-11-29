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

def set_defaults(params):
    keys = ['name', 'object']
    defaults = ['nmcli', 'networking']
    for key, default in zip(keys, defaults):
        if not params.get(key):
            params[key] = default

def run_module():
    module_args = dict(
        name =dict(type='str', required=False),
        object=dict(type='str', required=False),
        state =dict(type='str', required=False),
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

    set_defaults(module.params)
    result['original_message'] = f'{module.params}'
    result['message'] = 'tbd'
    changed = False
    failed = False

    if changed:
        result['changed'] = True

    if failed:
        module.fail_json(msg='Failed', **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
