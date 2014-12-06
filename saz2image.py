# -*- coding: utf-8 -*-
__author__ = 'nakatanakatana'

def filename(pattern, file):
    for l in file:
        m = pattern.search(l)
        try:
            filename = m.group(1)+m.group(2)
            return filename
        except:
            pass

def image(file):
    flag = False
    imdata = []
    for i in sfile:
        if not flag:
            if i == '\r\n':
                flag = True
        else:
            imdata.append(i)
    return imdata

if __name__ == '__main__':
    import os
    import re
    from zipfile import ZipFile
    saz_name = 'image.saz'
    dirname = saz_name.split('.')[0]
    z = ZipFile(saz_name)
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    cfilenames = [f for f in z.namelist() if f.endswith('c.txt')]
    sfilenames = [f for f in z.namelist() if f.endswith('s.txt')]
    re_img = re.compile('(\w*)(.jpg|.png|.gif)')
    for f in cfilenames:
        cfile = z.open(f)
        name = filename(re_img, cfile)
        if not f.replace('c.txt', 's.txt') in sfilenames:
            continue
        sfile = z.open(f.replace('c.txt', 's.txt'))
        imdata = image(sfile)
        if name and imdata:
            open(dirname+os.path.sep+name, 'wb').write(''.join(imdata))

