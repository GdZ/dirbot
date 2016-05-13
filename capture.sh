#!/bin/bash
ARGS=`getopt -o ab:c:: --long along,blong:,clong:: -n 'capture.sh' -- "$@"`
if [ $? != 0 ]; then
	echo "Terminating...."
	exit 1
fi

echo ${ARGS}
eval set -- "${ARGS}"
exit 0
action=$1
module=$2
echo action:${action}, module:${module}
case ${action} in
	'crawl')
		;;
	*)
		;;
esac

