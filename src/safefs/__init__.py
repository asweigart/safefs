"""SafeFS
By Al Sweigart al@inventwithpython.com

A Python module for safely working with the file system in a safe, auditable way."""

# TODO - SafeFS MUST work with Python 2.7.

__version__ = '0.1.0'

import uuid as uuid_module
import os, zlib

_DRY_RUN = False
_SAFE_ZONE = ()

def uuid():
    return str(uuid_module.uuid4())

guid = uuid  # guid() is an alias for uuid()

_UUID_OF_THIS_RUN = uuid()  # This uuid is kept for logging purposes.



def _logEvent(event):
    """
    logs all function calls made by this module
    """
    pass

def log(message, file=None, stdout=None):
    """
    for the user to log their own custom events TODO
    """
    pass


# TODO - should we call it "dry run" mode or "read only" mode?
# TODO - or have both? Dry Run mode is meant for logging, and has a separate log. Read only is meant for general safety.
# TODO - confirm mode will say "delete the above files" and prompt to stdout for manually confirmation


def enableDryRun():
    """
    TODO
    """
    global _DRY_RUN
    _DRY_RUN = True


def enableSafeZone(folders=None, includeSubfolders=True):
    """
    The "safe zone" is a folder (and optionally all the subfolders in it)
    that can be affected by safefs functions. Any write operations that happen
    outside of this safe zone will raise an OutsideSafeZone exception.
    TODO

    folder can be set to '.' to mean the safe zone is always the current working directory of the script
    folder can be set to '*' to mean everything is the safe zone and effectively sets safefs to read-only mode
    folder can also be an iterable to designate multiple folders. The includeSubfolders setting applies to all of
    them. (You can't have some folders include all subfolders and others not include them.)
    """
    pass


def disableSafeZone():
    """
    TODO
    """
    # TODO - returns the safe zone folder for later re-enabling
    pass


def enableConfirm():
    """
    Enables "confirmation mode", where any write actions outside the safe zone (if enabled) will prompt the user for manual confirmation.
    If the safe zone is not enabled, this will require confirmation for every write action.

    TODO - or maybe there should be a "confirm perimeter" and only things outside the perimeter? I don't want to over complicate this.
    """
    pass

def disableConfirm():
    pass


def strict():
    """
    TODO - Does enableConfirm() and enableSafeZone(cwd)
    """
    pass


def copy(src, dst, follow_symlinks=True):
    pass


cp = copy  # cp() is an alias for copy()


def move(src, dst):
    pass

mv = move  # mv() is an alias for move()


def delete(deleteThis, permanent=False):
    pass

# del() doesn't exist because del is a Python keyword.
rm = remove = delete  # rm() and remove() are aliases of delete()


def rename(renameThis):
    pass

ren = rename  # ren() is an alias of rename()


def exists(doesThisExist):
    pass



def home():
    pass


def cd(changeDirectoryToThis):
    pass

chdir = cd  # chdir() is an alias for cd()


def isdir():
    pass

def isfile():
    pass

def freespace():
    pass

def size(sizeOfThis):
    pass




def thumbprint(thumbprintOfThis):
    """
    TODO
    """
    if os.path.isfile(thumbprintOfThis):
        fileObj = open(thumbprintOfThis, 'rb')
        theThumbprint = zlib.adler32(fileObj.read())
        fileObj.close()
        return theThumbprint
    elif os.path.isdir(thumbprintOfThis):
        # TODO - what should the thumbprint of a folder be based off of? Just the filenames? Or also their sizes and contents? Maybe not, we don't include file metadata in the thumbprint of the file.
        lsBytes = str(os.listdir(thumbprintOfThis)).encode('utf-8')
        return zlib.adler32(lsBytes)


