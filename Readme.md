# dptools
This repository contains tools and notes for working with the leaked source code repositories for Pokémon Diamond and Pearl, mostly the prototype.

## Contents
- [`14032006`](14032006): Patches for the March 14th, 2006 source.
- [`scripts`](scripts): Scripts made for working with this repository and the prototype.

## Setup
This section will describe how to setup the leaked source code to compile and hack on the prototype.

### Prerequisites
- The original leaked CVS repository, for the source code.
- The easybuild package, for the SDK, Unix tools, and compiler.
  - This too comes with the source code, already checked out to a late point in development. This is different from the earlier prototype version that this repository assumes.
  - If you're a sucker for pain, you can try hunting down NitroSDK, NitroSystem, the Codewarriors DS compiler, and old versions of the Cygwin tools used (modern tools don't seem to really work), in place of easybuild.
- A Windows XP system.
  - I've documented my setup for this [here](https://gitlab.com/CodingKoopa/comet-observatory/-/blob/master/docs/QEMU%20Notes.md#windows-xp).
  - I've been told that there are distributions of whole VirtualBox images out there, with easybuild included and ready to go. Isn't technology amazing?
  - Other Windows versions (namely 7) may work, I haven't tested it though.
- [cvs2git](https://www.mcs.anl.gov/~jacob/cvs2svn/cvs2git.html) (you may find this included with a `cvs2svn` package).

### Instructions
These instructions are for Unix, but are applicable anywhere.

#### Converting the CVS repo to Git
1. Enter the CVS repo backup, to where you have, say, a `pokemon` directory containing `pokemon_dp` and/or `pm_dp_ose`.
2. Convert the CVS repo to a Git repo (the cvs2git step will take a long time!):
```sh
cvs2git --blobfile=git-blob.dat --dumpfile=git-dump.dat --fallback-encoding=shift_jis --username=cvs2git pokemon
cd ..
mkdir dp && cd dp
git init
git fast-import --export-marks=../pokemon/git-marks.dat < ../pokemon/git-blob.dat
git fast-import --import-marks=../pokemon/git-marks.dat < ../pokemon/git-dump.dat\
git checkout
```
See [here](https://www.mcs.anl.gov/~jacob/cvs2svn/cvs2git.html) and [here](https://www.mcs.anl.gov/~jacob/cvs2svn/cvs2svn.html) for more information.

#### Using and patching the prototype
1. Make a copy of `pm_dp_ose/include/library/spl*`. It will be needed to compile.
2. Using `git log` and `G` to go to the end of the pager, find the commit you want to work with (see the readmes for details), and `git checkout` to it.
3. Copy the SPL headers to `pm_dp_ose/include/library/`
4. Clone this repository.
```sh
git clone https://gitlab.com/CodingKoopa/dptools.git
```
4. Apply whatever patches you want, e.g. (from the DP source code directory):
```sh
git apply $PATH_TO_DPTOOLS/14032006/general_patches/*.patch
```

#### Modifying the code
This section gives some tips on modifying the code:
- Create a new branch from the 1st prototype commit, to work off of.
- You may have to manually re-`make` things sometimes. For instance, when editing the source files for scripts and text, they do not seem to get rebuilt automatically. [`scripts/.bash-rc`](scripts/.bash-rc) works around this by adding convenience functions to rebuild them unconditionally (accessed with `buildall`).