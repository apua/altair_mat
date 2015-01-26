"""
input content::

    http://15.226.124.71/deploy/rhel71-x64/addons/HighAvailability/TRANS.TBL

goal:

    generate a Powershell script to run on Windows2008R2/Powershell 2.0
    or newer version for downloading files in order

pre = """
$C = New-Object System.Net.WebClient
$P = (pwd).path
Function d($uri, $dir, $file) {
    $script:count ++
    $target = $dir + '/' + $file
    $dirpath = $P + '/' + $dir
    $filepath = $dirpath + '/' + $file
    echo ("({0,4}/${total}) ${target}" -f $count)
    mkdir -f $dirpath | Out-Null
    $C.DownloadFile($uri, $filepath)
}
""".lstrip()

url = 'http://15.226.124.71/deploy/'
uris = open('Info_rhel71-x64.csv').read().splitlines()
pre += "$count = 0\n"
pre += "$total = {}\n".format(len(uris))
for uri in uris:
    urn = uri.split(url,1)[1]
    dir, file = urn.rsplit('/',1)
    pre += 'd "{}" "{}" "{}"\n'.format(uri, dir, file)

with open('Info_rhel71-x64.ps1', 'w') as f:
    f.write(pre.replace('\n','\r\n'))
