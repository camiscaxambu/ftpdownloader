import urllib.request as req
import ftplib
import shutil
import os
from contextlib import closing

def customlistdir(path):
    url = path

    r= req.urlopen(url)
    k=r.read().splitlines()
    t=[str(s.decode('windows-1252','ignore')) for s in k]

    k=str(k)

    foo=t

    oslist=[]

    for i,each in enumerate(foo):
        if True:
            v=each.split("'")[0].strip()

            if '<DIR>'in v:
                V2=v.split('<DIR>')[-1].strip()
            else:
                V2=v.split(' ')
                nv2=[]

                for I,each in enumerate(V2):
                    try:
                        int(each)
                        break
                    except:
                        pass
                    nv2.append(each)
                V2=' '.join(V2[I+1:])
            oslist.append(V2)
    return oslist


def fileordir(nome):
    if '.' in nome:
        return 'file'
    else:
        return 'dir'

def download(url,name):
    req.urlretrieve(url,name)

def get_list(txt):
    nl=[]
    with open(txt, 'r') as file1:
        lines = file1.readlines()
        for v in lines:
            t=r'ftp://' + v.replace('\n','') + '@ftp.alfalaval.com/'
            nl.append(t)
        return nl
def main(bpath,url):
    try:
        os.mkdir(bpath)
    except:
        pass
    try:
        lcwd=customlistdir(url)
        for thing in lcwd:
            if fileordir(thing)=='dir':
                if(os.path.exists(bpath + '/' + thing + '/') == False):
                    print('creating folder: ', thing)
                    os.mkdir(bpath+'/'+thing+'/')
                print(bpath, 'folder: ', thing)
                nbpath=bpath+'/'+thing+'/'
                nurl=url+'/'+thing+'/'
                main(nbpath,nurl)
            elif fileordir(thing)=='file':
                try:
                    print('downloading file: ', thing)
                    download(url+thing,bpath+'/'+thing)


                except Exception as e:
                    print(thing ,'error :',e)
                    with open('cantdownload.txt', 'a') as f:
                        f.write(thing + "- ERROR - Can't download this file from the url" + url + str(e) + '\n')
    except Exception as v:
        print(url, "Error while trying to login")
        with open('log.txt', 'a') as f:
            f.write(url + "- Error while trying to login " + str(v) +'\n')

print("FTP DOWNLOADER ")

for i,url in enumerate(get_list('ftps.txt')):
    f = url.split('://')
    j = str(f[1]).split(':')
    main(str(j[0]),url)
