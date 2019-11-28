Config the new page
=========
##needed packages

* nginx
* Python 3.6
* vitualenv + pip
* Git

take an example in Ubuntu:

	sudo	add-apt-repository ppa:fkrull/deadsnakes
	sudo	apt-get install nginx git python36 python3.6-env

## Nginx virual env

* reference to nginx.template.conf
* replace SITENAME with domain name

## Systemd service

* refer to gunicorn-systemd.template.service
* replace SITENAME

##file structure

/home/username
	sites
		SITENAME
			database
			source
			static
			virtualenv
