[[ -z ${PROJECT_HOME} ]] && export PROJECT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. && pwd )"
PROJECT_SRC=${PROJECT_HOME}/src
echo "PROJECT_HOME: ${PROJECT_HOME}"
echo "PROJECT_SRC: ${PROJECT_SRC}"

# Empty the Sqlite3 DB in order to start from the beginning

[[ -f $PROJECT_SRC/db.sqlite3 ]] && rm -rf $PROJECT_SRC/db.sqlite3

if [[ -d $PROJECT_SRC/apps/users/migrations ]]; then
	pushd $PROJECT_SRC/apps/users/migrations > /dev/null
		rm -rf ./*
		touch __init__.py
	popd > /dev/null
else
	mkdir $PROJECT_SRC/apps/users/migrations
	pushd $PROJECT_SRC/apps/users/migrations > /dev/null
		touch __init__.py
	popd
fi

# Populates the DB with the new changes in models
pushd $PROJECT_SRC > /dev/null
	python manage.py makemigrations
	python manage.py migrate

	# Set the superuser creation non-interactive

	echo "Configuring non-interactive superuser creation."

	USER_APP_PATH=$PROJECT_SRC/apps/users
	MANAGEMENT_PATH=$USER_APP_PATH/management/commands

	if [[ -d ${MANAGEMENT_PATH} ]]; then
		echo "MANAGEMENT_PATH: is set on ${MANAGEMENT_PATH}"
	else
		echo "Creating management/commands folder"
		mkdir -p ${MANAGEMENT_PATH}
		echo "MANAGEMENT_PATH: has been set on ${MANAGEMENT_PATH}"
	fi

	touch $MANAGEMENT_PATH/__init__.py $MANAGEMENT_PATH/../__init__.py
	curl -sL https://gist.githubusercontent.com/c00kiemon5ter/7806c1eac8c6a3e82f061ec32a55c702/raw/0c8cebc17372f10d2764cd124caa5d9cee397fe6/create-superuser.py \
	-o $MANAGEMENT_PATH/create-superuser.py

	# Creates new super user with options as parameters.
	DJ_SUPERUSER_USERNAME=${USERNAME:-admin}
	DJ_SUPERUSER_EMAIL=${EMAIL:-admin@test.com}
	DJ_SUPERUSER_PASSWORD=${PASSWORD:-12345678}

	python manage.py create-superuser --username $DJ_SUPERUSER_USERNAME \
	--email $DJ_SUPERUSER_EMAIL \
	--password $DJ_SUPERUSER_PASSWORD
popd > /dev/null

# Added extra comment
