vagrant
=========

Install vagrant.

Requirements
------------

Debian OS (buster), VirtualBox.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - vagrant

To Test
-------
*requires docker, ansible, molecule[docker,lint]*

```(ansible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
