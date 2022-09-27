sys_upgrade
=========

Add contrib and non-free apt repositories, safe upgrade Debian system.

Requirements
------------

Debian OS (buster).

Role Variables
--------------

- ```deb_contrib_nonfree_repos``` debian source.list entries without last components.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - sys_ugrade

To Test
-------
*requires docker, ansible, molecule[docker,lint]*

```$ mol test```

License
-------

MIT

Author Information
------------------

2oleg.t@gmail.com
