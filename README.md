# Song-Genre-Classifier
A classifier for song genre detection using CNNs.

The GTZAN dataset was used for training the model.
Download from: http://opihi.cs.uvic.ca/sound/genres.tar.gz

The dataset consists of 30 second snippets of 1000 songs evenly spread across 10 genres.
The spectrogram_converter.py has the code for converting the songs into spectrograms.
The dataset.npz file is the numpy zip of the data.

Code for importing:<br>
<pre>
    import numpy as np
    data=np.load("dataset.npz")
    X=dataset['arr_0'] #spectrograms converted to np array
    y=dataset['arr_1'] #classes
</pre>
    
This approach yields a 77% accuracy on test set after training for 100 epochs.

The model.h5 file has the pretrained model that can be imported using tensorflow.
The model.png file has the network graph of the model.
