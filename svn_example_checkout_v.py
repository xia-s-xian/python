import pysvn
import time

client = pysvn.Client()


#check out the current version of the pysvn project

svn_file=3832
svn_url='http://10.0.2.88/svn/VimcBT/VA9638B/Src_Mod38/trunk/VA9638B_V8000_MultiCore'
client.checkout(svn_url,
    'F:/8.ZGW/4_VA9638项目/18_集成发布/VA9638B_V8000_MultiCore',revision=pysvn.Revision(pysvn.opt_revision_kind.number, svn_file))

