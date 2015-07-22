#! /bin/sh

dir=`dirname $0`
repo="altair-recipe"
version=`date +%Y%m%d`
tmp="/tmp"
filename=${repo}-${version}.zip
url="//csinfs.americas.hpqcorp.net/csi"
auth="csi%csi"

cd ${dir}
git archive --format zip master -o ${tmp}/${filename}

cd ${tmp}
smbclient ${url} -U ${auth} -c "cd ${repo} ; put ${filename}"
