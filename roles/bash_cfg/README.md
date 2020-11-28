bash_cfg
=========

Convigure Bash shell startup globaly.

Requirements
------------

Debian OS (buster).

Role Variables
--------------

- ```files2source``` files to be install into /etc/profile.d/

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - bash_cfg

To Test
-------

*requires docker, ansible, molecule[docker, lint]*

```(ansible) $ mol test```

License
-------

MIT

Author Information
------------------

o-le-g@inbox.ru
