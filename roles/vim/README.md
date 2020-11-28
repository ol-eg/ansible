vim
===

Install or upgrade vim, create global vimrc,
configure vim to be default editor systemwide.

Requirements
------------

Debian OS, ansible.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - vim

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
