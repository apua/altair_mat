def modify_ovf(fn):
    """
    Modify original .ovf file to support two indepent network with network adapters.

    This method should be called only when appliance IP and deployment IP are in different networks.

    It modifies .ovf file content manually without `xml.etree.ElementTree` or `lxml.etree`
    because those tools would make a total different new file from original one.

    This method is designed to be idempotent.

    @fn: the absolute path of OVF file
    """

    import hashlib
    import os
    import re
    import shutil

    def clean_check_backup(fn):

        # clean and check path
        assert os.path.isfile(fn), Exception("File doesn't exist.")

        # backup if it doesn't exist
        bak_fn = fn + '.bak'
        if not os.path.exists(bak_fn):
            shutil.copyfile(fn, bak_fn)


    ovf_fn, mf_fn = fn, os.path.splitext(fn)[0]+'.mf'
    for fn in (ovf_fn, mf_fn):
        clean_check_backup(fn)

    # get content
    content = open(ovf_fn).read()

    # modify *Network Section*
    patt = r'^(\s*<Network\s*ovf:name=")Template(".*?</Network>\s*)$'
    repl = lambda mat: '{0}Appliance{1}\n{0}Deployment{1}'.format(*mat.groups())
    content_ = re.sub(patt, repl, content, flags=re.DOTALL|re.MULTILINE)

    # modify *VirtualSystem Section*
    patt = r'(<rasd:Connection>)Template(</rasd:Connection>)'
    repl_app = lambda mat: '{0}Appliance{1}'.format(*mat.groups())
    repl_dep = lambda mat: '{0}Deployment{1}'.format(*mat.groups())
    content__  = re.sub(patt, repl_app, content_ , count=1)
    content___ = re.sub(patt, repl_dep, content__, count=1)

    # write down modified content
    with open(ovf_fn, 'w') as f:
        f.write(content___)

    # count SHA1 value and write down to .mf file
    val = hashlib.sha1(content___).hexdigest()
    value_changed = re.sub(r'(?<=ovf\)= ).*', val, open(mf_fn).read())
    with open(mf_fn, 'w') as f:
        f.write(value_changed)


if __name__=='__main__':
    filename = '/ovf/ICsp-vmware-7.4.1-20141113/ICsp-vmware-7.4.1-20141113.ovf'
    modify_ovf(fn=filename)
