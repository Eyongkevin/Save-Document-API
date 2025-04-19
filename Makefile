dev-start:
	export FLASK_APP="src.apps.__init__.py"  && python -m wsgi run --debug
db-init:
	export FLASK_APP="src.apps.__init__.py" && flask db init
db-migrate:
	export FLASK_APP="src.apps" && flask db migrate
db-upgrade:
	export FLASK_APP="src.apps" && flask db upgrade
dev-install:
	pip install -r requirements/dev.txt
test-install:
	pip install -r requirements/test.txt