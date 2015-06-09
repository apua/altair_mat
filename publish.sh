repo=altair-recipe
version=0.1
tmp=/tmp
filename=${repo}-${version}.zip

cd ~/${repo}
git archive --prefix=${repo}/ --format zip master -o ${tmp}/${filename}

cd ${tmp}
smbclient //csinfs.americas.hpqcorp.net/pub -U csi%csi -c "cd ${repo} ; put ${filename}"
