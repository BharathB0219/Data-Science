import numpy as np
import pandas as pd
a={'Maths':[60,78,90,65],
   'Science':[89,67,98,20],
   'English':[90,87,89,70],
   'History':[87,90,76,87]}
score=pd.DataFrame(a)
print(score)
average=np.mean(a['Maths']),np.mean(a['Science']),np.mean(a['English']),np.mean(a['History'],axis=0)
print("Average of each subject",average)
highest=np.argmax(average)
highestscore=average[highest]
print("Subject with highest score:",highestscore)

