import docclass
from subprocess import check_output

cl = docclass.naivebayes(docclass.getwords)
#remove previous db file
check_output(['rm', 'TrainingSpam.db'])

cl.setdb('TrainingSpam_out.db')
docclass.spamTrain(cl)

#classify text: "the banking dinner" as spam or not spam
print( cl.classify('twitter') )
