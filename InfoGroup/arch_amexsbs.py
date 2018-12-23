import subprocess
import threading
import time
import os, sys
import datetime
import Queue
import shutil

amexintl_div_id = 946509
amexintl_client_id = 10165578
amexintl_process_inputfiles = 'SBS_ARCHIVE_INPUTFILES'
amexintl_process_outputfiles = 'SBS_ARCHIVE_OUTPUTFILES'
amexintl_process_workfiles = 'SBS_ARCHIVE_WORKFILES'

amexintl_inputfiles_path = '/data/datafiles/mzp/amexsbs/archive/inputfiles'
amexintl_outputfiles_path = '/data/datafiles/mzp/amexsbs/archive/outputfiles'
amexintl_workfiles_path = '/data/datafiles/mzp/amexsbs/archive/workfiles'
amexintl_retention_2yrs = 760



class uploaderThread (threading.Thread):

    def __init__(self, threadID, threadName,division_id,client_id,process_id,retention_days,q):
        threading.Thread.__init__(self)
        self.threadID       = threadID
        self.threadName     = threadName
        self.division_id    = division_id
        self.client_id      = client_id
        self.process_id     = process_id
        self.retention_days = retention_days
        self.q = q

    def run(self):
        print "Starting " + self.threadName,
        fileUploder(self.threadName,self.division_id,self.client_id,self.process_id,self.retention_days,self.q)


def fileUploder(threadName,division_id,client_id,process_id,retention_days,q):

    process_arg     = '-pri={0}'.format(process_id)
    division_arg    = '-div={0}'.format(division_id)
    client_arg      = '-cst={0}'.format(client_id)
    retention_arg   = '-rpd={0}'.format(retention_days)

    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            fileName = q.get()
            file_arg = '-fle={0}'.format(fileName)
            queueLock.release()
            call_str = '/data/programs/generic/scripts/shell/MzpFileProc.sh -cfg=mzp_sch.cfg -sch=2 {0} ' \
                       ' {1}  {2} {3} {4} -qnm=EFTEVENT.QUEUE'.format(file_arg,process_arg,division_arg,client_arg,retention_arg)
            subprocess.call(call_str, shell=True, cwd='/data/programs/generic/scripts/shell')

            print "%s processing %s" % (threadName, fileName)
        else:
            queueLock.release()
        time.sleep(1)

if __name__ == '__main__':

    threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6"]
    queueLock = threading.Lock()
    workQueue = Queue.Queue(0)
    now = time.time()
    # cutoff = 60 days
    inputfiles_dict = {"process" : amexintl_process_inputfiles, "nirvana" : 'y', "cutoff" : 60, "path" : amexintl_inputfiles_path}
    outputfiles_dict = {"process": amexintl_process_outputfiles, "nirvana" : 'y', "cutoff" : 60, "path" : amexintl_outputfiles_path}
    workfiles_dict = {"process" : amexintl_process_workfiles, "nirvana" : 'y', "cutoff" : 60, "path" : amexintl_workfiles_path }

    processes = [inputfiles_dict, outputfiles_dict, workfiles_dict ]

    for p in processes:

        exitFlag = 0
        count = 0
        threads = []
        threadID = 1
        filesToRemove = []

        removeBeforeDays = p["cutoff"]
        # Calculated cut off date
        cutoff = now - (removeBeforeDays * 86400)

        process_id   = p["process"]
        process_path = p["path"]
        nirvana      = p["nirvana"]
        print "------------------------------------------------------------------------------------"
        print "STARTING : "+process_id +": "+nirvana + ": "+ process_path
        print "------------------------------------------------------------------------------------"
        if nirvana == "y":
            # Create new threads
            for tName in threadList:
                thread = uploaderThread(threadID, tName,amexintl_div_id,amexintl_client_id,process_id, amexintl_retention_2yrs, workQueue)
                thread.start()
                threads.append(thread)
                print 'threadID = {0}'.format(threadID)
                threadID += 1


        # Fill the queue
        queueLock.acquire()

        # Processing files
        for f in os.listdir(process_path):
          if os.stat(process_path + '/' + f).st_mtime < cutoff:
              if os.path.isfile(process_path + '/' + f):

                  filesToRemove.append(f)
                  print "File Name = " + f
                  print datetime.datetime.fromtimestamp(os.stat(process_path + '/' + f).st_mtime)
                  count += 1
                  if nirvana == "y":
                    workQueue.put(f)
                  print "Count = {0}".format(count)

        queueLock.release()

        # Wait for queue to empty
        while not workQueue.empty():
            pass

        # Notify threads it's time to exit
        exitFlag = 1

        # Wait for all threads to complete
        for t in threads:
            t.join()

        if os.path.isdir(process_path + '/' +'deleted') == False:
            os.mkdir(process_path + '/' +'deleted',0777)
        # elif:
        #     os.remove(amexintl_inputfiles_path + '/' +'deleted')
        #     os.mkdir(amexintl_inputfiles_path + '/' + 'deleted', 777)

        for f in filesToRemove:
            print "Moving file " + f
            shutil.move(process_path + '/' +f,process_path + '/' +'deleted'+'/'+f)

    print "Exiting Main Thread"

