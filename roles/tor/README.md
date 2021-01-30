tor
===

Install TOR browser.

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- ```tor_aliases```   : aliases to be added to users bash config.
- ```backports```     : debian backports apt source.
- ```homedir_prefix```: default: /home.
- ```tor```           : debian tor launcher package name.
- ```users```         : list of users to have tor cmd aliases.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - { role: tor, users: [mort] }

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
