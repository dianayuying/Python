"""
Convert seconds to hh:mi:ss format
"""
def make_readable(seconds):
    return str(int(int(seconds/60)/60)).zfill(2)+":"+str(int(seconds/60)%60).zfill(2)+":"+str(seconds%60).zfill(2)