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
'''
head = pysvn.Revision(pysvn.opt_revision_kind.number, old_rev)
end = pysvn.Revision(pysvn.opt_revision_kind.number, new_rev)

log_messages = client.log(work_path, revision_start=head, revision_end=end,
        limit=0)
for log in log_messages:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log.date))
    print ('[%s]\t%s\t%s\n  %s\n' % (log.revision.number, timestamp,
            log.author, log.message))
print

FILE_CHANGE_INFO = {
        pysvn.diff_summarize_kind.normal: ' ',
        pysvn.diff_summarize_kind.modified: 'M',
        pysvn.diff_summarize_kind.delete: 'D',
        pysvn.diff_summarize_kind.added: 'A',
        }

print( 'file changed:')
summary = client.diff_summarize(work_path, head, work_path, end)
for info in summary:
    path = info.path
    if info.node_kind == pysvn.node_kind.dir:
        path += '/'
    file_changed = FILE_CHANGE_INFO[info.summarize_kind]
    prop_changed = ' '
    if info.prop_changed:
        prop_changed = 'M'
    print (file_changed + prop_changed, path)
print
'''
