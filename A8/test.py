import docclass
from subprocess import check_output

cl = docclass.naivebayes(docclass.getwords)
#remove previous db file
check_output(['rm', 'TestingSpam1.db'])

cl.setdb('TestingSpam1.db')
docclass.spamTrain(cl)

#classify text: "the banking dinner" as spam or not spam
print( cl.classify('the banking dinner') )
