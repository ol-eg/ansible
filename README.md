# ansible

## install (debian host assumed)
*create ansible user, add it to the sudo group and make sudo passwordless*
```bash
# adduser ansible
# usermod -a -G sudo ansible
# echo 'ansible ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/ansible
```
```bash
$ sudo apt install python3-venv python3-virtualenv git
$ sudo su - ansible
$ mkdir -v ~/.virtualenvs
$ python3 -m venv ~/.virtualenvs/ansible
$ source ~/.virtualenvs/ansible/bin/activate
(ansible) $ pip install --upgrade pip setuptools wheel
(ansible) $ pip install ansible
```
### install playbooks and private roles
```bash
(ansible) $ git clone https://github.com/ol-eg/ansible.git && cd ansible
(ansible) $ git config credential.helper store
(ansible) $ for role_name in o.sys-upgrade o.bash-cfg o.molecule; do
(ansible) > ansible-galaxy install git+https://github.com/ol-eg/${role_name}.git
(ansible) > done
```
### play
```
(ansible) $ ansible-playbook playbooks/debian-laptop.yaml
```
