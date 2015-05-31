import re
import os
import glob
import sys
import nltk

datapath = ['./']
for document_path in datapath:
        for document_file in glob.glob(os.path.join(document_path, '*.txt')):
            mockingJay = []
            #f = io.open(document_file, "r+", encoding='utf-8')
            f = open(document_file, "r")                
            print "Reading file ... ",os.path.basename(document_file)
            s = f.read()
            # mockingJay = re.split(r"\.\s*", s)
            mockingJay = nltk.sent_tokenize(s)

            new_filename = "./"+"Summaries"+os.path.basename(document_file).split('.')[0]+'.txt'

            print "Writing to file...", os.path.basename(new_filename)
            s = ""
            #print mockingJay, "\nd"
            with open(new_filename, "w+") as f2:
                for ele in mockingJay:
                    s += ele + "\n"
                f2.write(s)
            print ("-------------------------------------------------------------")
            f.close()
