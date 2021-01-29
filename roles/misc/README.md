misc
====

Install miscellaneous tools which require no configuration.

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- **tools**: os packages to be installed

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - { role: misc }

To Test
-------

requires:
- os packages: docker
- python packages: ansible, molecule.

```(asible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
