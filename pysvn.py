#pysvn Programmer's Guide：http://pysvn.tigris.org/docs/pysvn_prog_guide.html
import time
import pysvn
#import svn.remote


muli_core='F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore'
dsp='D:/4_ZGW/VimcBT/VA9638B/Src_DSP/BTAudio_Digitalgain'

work_path = 'F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore'
url='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/branches/VA9638B_V8009_UI'

client = pysvn.Client()

entry = client.info(work_path)
old_rev = entry.revision.number

rev=pysvn.Revision( pysvn.opt_revision_kind.number,3832)
revs = client.update(work_path,rev)
new_rev = revs[-1].number-1
#revs = client.update(work_path,revision=new_rev)
print(revs)

print( 'updated from %s to %s.\n' % (old_rev, new_rev))

def revert_svn_ver():
    client.revert(path,recurse=True)

def clean_up_svn():
    client.cleanup(path,fix_recorded_timestamps=True, clear_dav_cache =True,vacuum_pristines=True, include_externals=True)
