dev-start:
	export FLASK_APP="src.apps.__init__.py"  && python -m src.manage run --debug
db-init:
	export FLASK_APP="src.apps" && flask db init
db-migrate:
	export FLASK_APP="src.apps" && flask db migrate
db-upgrade:
	export FLASK_APP="src.apps" && flask db upgrade
dev-install:
	pip install -r requirements/dev.txt