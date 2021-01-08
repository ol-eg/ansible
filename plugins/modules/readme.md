*from this directory*

[NetworkManager module](./nm.py) is rather educational exercise.
There's no real need for it except for documenting nmcli commands.

Unit Tests
----------

```(ansible) $ pytest [--cov=. --flake8 --cov-report=html]```

Type Check
----------

```(ansible) $ mypy --module nm```

Check DocStrings
----------------

```(ansible) $ ansible-doc --type=module nm```

To install
----------

```bash
(ansible) $ ansible-galaxy collection install git@github.com:ol-eg/ansible.git
```

*make sure path to
```~/.ansible/collections/ansible_collections/oppa/all/plugins/modules```
is configured in ansible.cfg::library*
