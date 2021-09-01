from __future__ import division, print_function
import pytest
import safefs




"""
Accepts globs, files or folders.
Does all the things shutil and os does.
Supports pathlib

EASY TO UNDERSTAND ERROR MESSAGES

copy() cp() has follow_symlink
move() mv()
rm() remove() delete()
rename() ren()
exists()
home()
isfile()
isdir()
issame()
isblank()
freespace()
size()
touch()
home()
cd()
cwd()

ls() / dir()


extension()/base()

walk()

download()

write()
append()
read()
readlines()

guid() uuid()

log()
logsFromThisRun()
openLog() (also returns the filepath)
logFile()
log events always show the exact function call and file/line number, but then also the absolute file path
log as a json file?
I should research logly and other popular logging systems.


dry filesystem is a list of lists


mtime()
atime()
ctime()

hooks - on del/move/rename/copy/touch
follow

thumbprint(file or folder) - crc()
sha()


>>> when i wrote a content-addressable store, one of the things i did was crib rsync's style of atomic overwrites (ie you write a temp file and rename() it into position)

"""





def test_basic():
    safefs.issame('same1.txt', 'same2.txt')
    safefs.issame()
    safefs.copy('hello.txt', 'deleteme.txt')
    safefs.rm('')
    safefs.touch('deleteme.txt')



    pass  # TODO - add unit tests



if __name__ == "__main__":
    pytest.main()
