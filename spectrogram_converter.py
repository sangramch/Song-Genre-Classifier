import os
import sys
from subprocess import check_call
from tempfile import mktemp
from scipy.io import wavfile
import matplotlib.pyplot as plt
from pydub import AudioSegment

folderpath="/run/media/sangram/Games and Study Materials/Projects/Song Genre Classifier/genres/"
outpath="/run/media/sangram/Games and Study Materials/Projects/Song Genre Classifier/spectro/"

folderlist=os.listdir(folderpath)

for foldername in folderlist:
    filepath=folderpath+foldername+"/"
    filelist=os.listdir(filepath)
    
    for filename in filelist:
        
        aufilepath=filepath+filename
        
        wname = mktemp('.wav')
        sound=AudioSegment.from_file(aufilepath,'au')
        sound.export(wname,format="wav")
        samplingfreq,signaldata= wavfile.read(wname)
        os.unlink(wname)
        
        if(len(signaldata.shape)==2):
            signaldata=signaldata[:,0]
        
        fig=plt.figure(frameon=False)
        
        ax=plt.Axes(fig, [1.,1.,1.,1.])
        fig.set_size_inches(6,1)
        ax.set_axis_off()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        fig.add_axes(ax)
        
        ax.specgram(signaldata, Fs=samplingfreq, NFFT=1024, noverlap=0 ,cmap="gray")
        
        imgfilename=outpath+foldername+"/"+filename[:-3]+'.png'
        fig.savefig(imgfilename,bbox_inches='tight',pad_inches=0,dpi=128)
        plt.close(fig)