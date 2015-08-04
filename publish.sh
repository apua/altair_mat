#! /bin/sh

# Run :code:`sh publish.sh` to publish this git repository to FTP through SMB.

dir=`dirname $0`
repo="altair-recipe"
version=`date +%Y%m%d`
tmp="/tmp"
filename=${repo}-${version}.zip

#url="//csinfs.americas.hpqcorp.net/csi"
#auth="csi%csi"
url="csinfs.americas.hpqcorp.net/${repo}"
auth="csi,csi"

cd ${dir}
git archive --format zip master -o ${tmp}/${filename}

cd ${tmp}
#smbclient ${url} -U ${auth} -c "cd ${repo} ; put ${filename}"
lftp -u ${auth} -e "put ${filename};ls;quit" ${url}
