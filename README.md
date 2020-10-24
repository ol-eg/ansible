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

ssh public key needs to be uploaded to git hub via web-frontend (settings -> SSH and GPG keys)

```bash
(ansible) $ git clone git@github.com:ol-eg/ansible.git && cd ansible
(ansible) $ for role in o.sys-upgrade o.bash-cfg o.docker o.molecule; do
(ansible) > ansible-galaxy install git+git@github.com:ol-eg/${role}.git
(ansible) > done
```
### play
```
(ansible) $ ansible-playbook playbooks/debian-laptop.yaml
```
