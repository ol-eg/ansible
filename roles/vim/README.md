vim
===

Install or upgrade vim-nox.
Configure vim to be default editor systemwide.
For the target user configure vim for python.

Requirements
------------

Debian OS, ansible.

Role Variables
--------------

*defaults are in* ```./defaults/main.yml```

- **fonts**: nerd fonts
- **homedir_prefix**: user homes directory
- **lines**: Vim commands for global config
- **patterns**: techical var shodow of **lines**
- **prerequisites**: os packages to be installed
- **sys_font_dir**: system fonts directory
- **sys_vimrc**: path to systemwide vim config file
- **users**: list of users which vim is to be configured for
- **vundle_dir**: vundle installation directory
- **vundle_repo_url**: github url
- **vundle_version**: vundle version to be installed

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
