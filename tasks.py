# -*- coding: utf-8 -*-
'''inv matter for auto pub. 101.camp
'''

__version__ = 'blog101CAMP v.200306.2042'
__author__ = 'Zoom.Quiet'
__license__ = 'CC-by-nc-nd@2019-09'

#import io
import os
#import re
import sys
import time
#import datetime
#import json
#import marshal as msh
#import subprocess
#import logging

#import sys
import logging
#logging.basicConfig()
logging.basicConfig(level=logging.CRITICAL)
_handler = logging.StreamHandler()
_formatter = logging.Formatter("[%(levelname)s]%(asctime)s:%(name)s(%(lineno)s): %(message)s"
                #, datefmt='%Y.%m.%d %H:%M:%S'
                , datefmt='%H:%M:%S'
                )
_handler.setFormatter(_formatter)
LOG = logging.getLogger(__name__)
#LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)  
LOG.propagate = False

LOG.addHandler(_handler)
#LOG.debug('load LOG level')







from pprint import pprint as pp
#pp = pprint.PrettyPrinter(indent=4)
from pprint import pformat

#import platform
#os_name = platform.system()
#del platform

#import subprocess





from invoke import task
#from fabric.context_managers import cd
from textwrap import dedent as dedentxt

CAMPROOT = os.environ.get("CAMPSITES_ROOT")
CSITES = {'blog':{'ori':'blog'
                , 'ghp':'blog_ghp'
                }
        }

AIM = 'site'
_TRIP = '_trigger'
_TOBJ = 'deploy.md'
TRIGGER = 0

LOCSITES = os.environ.get("LOCSITES")
ANNS = [# MkDocs
        {'aim':'blog.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/blog",
            'ann':"mkdocs_alabaster/inc/announce.html",
            },
        {'aim':'101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/gl_101.camp",
            'ann':"_theme/material/partials",
            },
        {'aim':'py.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/gl_py.101.camp",
            'ann':"_theme/bootswatch/simplex",
            },

        {'aim':'gui.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/gui.101.camp",
            'ann':"_theme/bootswatch/simplex",
            },
        {'aim':'dj.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/django",
            'ann':"_theme/bootswatch/simplex",
            },
        {'aim':'wr.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/writer",
            'ann':"_theme/bootswatch/simplex",
            },

        {'aim':'tm.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/_running/TM/tm",
            'ann':"custom_material/inc",
            },

    #, Jekyll
        {'aim':'du.101.camp/duw',
            'depoly':'pub4trigger.sh',
            'root':"DU.xmq/debuguself.github.io",
            'ann':"_includes",
            },

        {'aim':'fm.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/FM/fm",
            'ann':"_includes",
            },
        {'aim':'devrel.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"101.camp/devrel.info",
            'ann':"_includes",
            },
            
        {'aim':'blog.zhgdg.org',
            'depoly':'pub4trigger.sh',
            'root':"org.zhgdg/blog",
            'ann':"_includes",
            },
        {'aim':'zh.tfug.world',
            'depoly':'pub4trigger.sh',
            'root':"TFUG.ZH/zh.tfug.world",
            'ann':"_includes",
            },
        {'aim':'ydlj.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"YueDuLinJu/yuedulinju.github.io",
            'ann':"_includes",
            },

    #, 'fab'/Pelican
        {'aim':'blog.zoomquiet.io',
            'depoly':'pub4trigger.sh',
            'root':"zoomquiet.io/blog",
            'ann':"_themes/pelican-bootstrap3/templates/includes",
            },
        {'aim':'du.101.camp',
            'depoly':'pub4trigger.sh',
            'root':"DU.xmq/DUW/br_duw_pub",
            'ann':"_theme/mkdocs_alabaster/inc",
            },

        {'aim':'blog.PyChina.org',
            'depoly':'pub4trigger.sh',
            'root':"PyChina.org/blog",
            'ann':"_themes/pelican-bootstrap3/templates/includes",
            },
        {'aim':'weekly.PyChina.org',
            'depoly':'pub4trigger.sh',
            'root':"PyChina.org/weekly",
            'ann':"_themes/pelican-bootstrap3/templates/includes",
            },


]





@task 
def ver(c):
    '''echo crt. verions
    '''
    print('\n\t powded by {}'.format(__version__))


#   support stuff func.
def cd(c, path2):
    os.chdir(path2)
    print('\n\t crt. PATH ===')
    c.run('pwd')

#@task 
def ccname(c):
    c.run('cp CNAME %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')

#@task 
def sync4media(c):
    c.run('cp -rvf img %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')


#@task 
def pl(c, site):
    '''$ inv pl [101|py] <- pull all relation repo.
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    if site:
        #pp(CSITES[site])
        
        _aim = '%s/%s'%(CAMPROOT, CSITES[site]['gl'])
        cd(c, _aim)
        #os.chdir(_aim)
        #c.run('pwd')
        c.run('git pull', hide=False, warn=True)
        _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
        cd(c, _aim)
        #os.chdir(_aim)
        #c.run('pwd')
        c.run('git pull', hide=False, warn=True)
    else:
        ver(c)


@task 
def ann(c):
    '''$ inv ann <- sync announce.html all sites
    '''
    global CAMPROOT
    global CSITES
    global LOCSITES
    global ANNS
    _root = '%s/%s'%(CAMPROOT, CSITES['blog']['ori'])
    print(_root)
    #cd(c, _aim)
    
    pp(ANNS[0])
    print(len(ANNS))
    _orig = '%s/%s'%(_root, ANNS[0]['ann'])
    print(_orig)
    
    for s in ANNS[1:]:
        _upd = '%s/%s/%s'%(LOCSITES, s['root'] , s['ann'])
        print('\n',s['aim'])
        c.run('cp -v %s %s/ '%(_orig, _upd) )
        _deploy = '%s/%s/%s'%(LOCSITES, s['root'], s['depoly'])
        print(_deploy)
        c.run(_deploy)
        
    cd(c, _root )
    c.run('python -V')

    return None
    
    _site = ANNS[0]
    print('sync =>', _site['aim'])
    print('\t', _site['root'])
    
    _deploy = '%s/%s/%s'%(LOCSITES, _site['root'], _site['depoly'])
    print(_deploy)
    c.run(_deploy)
    
    cd(c, _root )
    c.run('python -V')
    #c.run('pwd')
    return None
    #c.run('mkdocs  -q  build', hide=False, warn=True)

@task 
def bu(c, site):
    '''usgae MkDocs build AIM site
    '''
    reidx(c, site)
    c.run('pwd')
    c.run('mkdocs  -q  build', hide=False, warn=True)

#@task 
def pu(c):
    '''push original branch...
    '''
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )

    c.run('pwd')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
          '"inv(loc) MkDocs upgraded by DAMA (at %s)"'% _ts
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#   'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '
#@task 
def gh(c, site):
    '''$ inv gh [101|py] <- push gh-pages for site publish
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    
    ccname(c)
    #sync4media(c)
    
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )
    
    _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
    cd(c, _aim)
    #os.chdir(AIM)
    #with cd('site/'):
    #c.run('pwd')
    c.run('ls')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
          '"pub(site) gen. by MkDocs as invoke (at %s)"'% _ts
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#@task
def chktri(c):
    '''check trigger obj. set TRIGGER switch
    '''
    global TRIGGER
    global _TRIP, _TOBJ
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _path =  './%s'% _TRIP
    print(_path)
    #print(os.listdir(_path))
    #print(type(os.listdir(_path)))
    if _TOBJ in os.listdir(_path):
        print('\n\tTRIGGERed by %s exist'% _TOBJ)
        TRIGGER = 1
    else:
        print('\n\tTRIGGER obj. -> %s ~> NOT exist\n\t CANCEL build...'% _TOBJ)
        TRIGGER = 0

#@task
def recover(c):
    '''recover trigger state, by del TRIGGER obj.
    '''
    global TRIGGER
    global _TRIP, _TOBJ
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _path =  './%s'% _TRIP
    _obj =  '%s/%s'%(_path, _TOBJ)
    print(_obj)
    c.run('rm -vf %s'% _obj)
    c.run('ls -Aogh %s'% _path)

    c.run('git st')
    c.run('git fix "(pubDUW) recover trigger obj. wait NEXT deploy"')

    TRIGGER = 0
    print('TRIGGER obj. recover -> waiting human deploy again')


def _injector(aim, drug):
    '''inject drug into aim .md
    ::.
        <- here
    .::
    '''
    _TS = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                 , str(time.time()).split('.')[1][:3] )
    #print(aim,drug)
    _exp = ''
    _replace = 0
    for l in open(aim):
        #print(l)
        if '::.' == l[:-1]:
            print('start inject')
            _replace = 1
            _exp += l 
        elif '.::' == l[:-1]:
            _replace = 0
            _exp += "\n"+drug
            print(drug)
            _exp += '\n\n(auto index injected at %s) \n\n'% _TS
            _exp += l 
            print('end inject')
        else:
            if _replace:
                pass
            else:
                _exp += l 
            
    #print(_exp)
    open(aim,'w').write(_exp)
    return None


#@task
def reidx(c, site):
    '''re-build _index auto.
    '''
    #global TRIGGER
    global _TRIP, _TOBJ

    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _crt = '%s/%s'%(CAMPROOT, CSITES[site]['ori'])
    _doc = '%s/docs'%_crt
    #print(_doc)
    _lasted = {}
    for root, dirs, files in os.walk(_doc):
        '''for d in dirs:
            pp(d)
        for f in files:
            pp(f)
        '''
        if len(dirs) > 0:
            #print('as startting...')
            continue
        else:
            pp(root)
            #print(root.split('/'))
            _sub = root.split('/')[-1]
            
            pp(dirs)
            _idx = []
            for f in files:
                if 'index.md' == f:
                    pass
                else:
                    _md = "%s/%s"%(root,f)
                    #print(_md)
                    #print(f.split('-'))item
                    _item = '- [{}]({})'.format(open(_md).readlines()[0][1:-1]
                                    , f)
                    _fn = f.split('-')
                    _r2li = '- [{}]({}/{})'.format(open(_md).readlines()[0][1:-1]
                                    ,_sub
                                    , f)
                    if len(_fn[0])==6 and len(_fn)>=2:
                        #print(_fn)
                        if _fn[0] in _lasted:
                            #print(_lasted[_fn[0]])
                            _lasted[_fn[0]].append(_r2li)
                            #print(_lasted[_fn[0]])
                        else:
                            _lasted[_fn[0]] = []
                            _lasted[_fn[0]].append(_r2li)
                    #print(_itme)
                    #print(_r2li)
                    _idx.append(_item)
            #pp(files)
            #pp(_idx)
            _aim = "%s/index.md"%root
            _injector(_aim, '\n'.join(_idx))
        #print('\n\tanothers levels...\n')




    #pp(_lasted)
    _top = 7
    _update = []   
    #pp(sorted(_lasted,reverse=True))
    for i in sorted(_lasted,reverse=True) : 
        if _top == 0: break
        _top -= 1
        #print(i, _lasted[i]) 
        _update.append('\n'.join(_lasted[i]))
    
    #pp('\n'.join(_update))
    _aim = '%s/index.md'%_doc
    print('\n\t _injector', _aim)
    _injector(_aim, '\n'.join(_update))
    
    return None
    #print(os.listdir(_path))
    #print(type(os.listdir(_path)))
    if _TOBJ in os.listdir(_path):
        print('\n\tTRIGGERed by %s exist'% _TOBJ)
        TRIGGER = 1
    else:
        print('\n\tTRIGGER obj. -> %s ~> NOT exist\n\t CANCEL build...'% _TOBJ)
        TRIGGER = 0

@task 
def pub(c, site):
    '''$ inv pub blog <- auto deploy new site version base multi-repo.
    '''
    global TRIGGER
    global CAMPROOT
    global CSITES
    #print(CAMPROOT)
    #pl(c, site)
    _crt = '%s/%s'%(CAMPROOT, CSITES[site]['ori'])
    cd(c, _crt)
    chktri(c)
    
    if TRIGGER:
        print('auto deplo NOW:')
        #return None
        bu(c, site)
        recover(c)

        pu(c)
        #ccname(c)
        #sync4media(c)
        gh(c, site)
        ver(c)

    else:
        print('nothing need deploy')
    
    return None



