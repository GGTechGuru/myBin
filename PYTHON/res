#! /usr/bin/python
import os
import sys

pid=os.fork()

if pid==0:

    os.chdir(os.environ["HOME"] + "/Documents/RESUME")

    pid2=os.fork()
    if pid2==0:

        from datetime import datetime, date, time

        allFiles = [fn for fn in os.listdir(".") if os.path.isfile(fn) ]

        latestSwdevTime = datetime.min
        latestSwengrTime = datetime.min

        for fn in allFiles:
            if "SoftwareDeveloper" in fn:
                modTime = datetime.fromtimestamp(os.stat(fn).st_mtime)

                if modTime > latestSwdevTime:
                    latestSwdevTime = modTime 
                    latestSwdevFn = fn

                continue

            if 'SoftwareEngineer' in fn:
                modTime = datetime.fromtimestamp(os.stat(fn).st_mtime)
                if modTime > latestSwengrTime:
                    latestSwengrTime = modTime 
                    latestSwengrFn = fn

                continue


        with open("/tmp/resList", "w") as resList:
            resList.write(latestSwdevFn + "\n")
            resList.write(latestSwengrFn + "\n")

        sys.exit(0)

    #####################################

    from subprocess import call

    cpid = os.wait()
    # flist = open("/tmp/resList", "r").readlines()
    flist = open("/tmp/resList", "r").read().splitlines()

    # print(os.getpid())
    print(flist)
    for fn in flist:

        fn = fn.strip()
        fnpath = os.path.join(os.getcwd(), fn.strip())

        # print fnpath
        # call(["soffice", fnpath])
        os.spawnlp(os.P_NOWAIT, "soffice", "soffice", fnpath)
