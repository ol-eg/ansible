bash_cfg
=========

Convigure Bash shell startup for users.

Requirements
------------

Debian OS (buster).

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- ```homedir_prefix``` default: /home
- ```startups```       files to be install into each user $HOME
- ```users```          list of users

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - { role: bash_cfg, users: [mort, ansible] }

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
