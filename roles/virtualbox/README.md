virtualbox
=========

Install virtualbox from Oracle repo.
https://wiki.debian.org/VirtualBox#Debian_10_.22Buster.22

Requirements
------------

Debian OS (buster).

Role Variables
--------------

- ```apt_src_lst_dir```     Apt sources list dir, default: /etc/apt/sources.list.d
- ```vb.apt_src_lst_name``` VirtualBox source name, default: virtualbox
- ```vb.src_entry```        Apt source entry, default: "deb http://download.virtualbox.org/virtualbox/debian buster contrib"
- ```vb.pgp_url```          VirtualBox PGP Public Key URL, default: https://www.virtualbox.org/download/oracle_vbox_2016.asc
- ```vb.pkg_name```         VirtualBox package to be installed, default: virtualbox-6.0

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
         - virtualbox

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
