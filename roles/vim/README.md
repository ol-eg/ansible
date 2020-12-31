vim
===

Install or upgrade vim-nox.
Configure vim to be default editor systemwide.
For the target user configure vim for python.

Requirements
------------

Debian OS, ansible.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - { role: vim, users: [ansible,scrat] }

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
