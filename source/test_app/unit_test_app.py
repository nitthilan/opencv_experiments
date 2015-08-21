#!/usr/bin/python
import unittest
import os
from os import listdir
from os.path import isfile, join
import pickle
 
class FooTest(unittest.TestCase):
    """Sample test case"""
     
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "FooTest:setUp_:begin"
        ## do something...
        print "FooTest:setUp_:end"
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "FooTest:tearDown_:begin"
        ## do something...
        print "FooTest:tearDown_:end"
     
    # test routine A
    def testA(self):
        """Test routine A"""
        print "FooTest:testA"
        os.system("python imagecleaning.py input/IMG_20141220_184526098.jpg output/IMG_20141220_184526098.jpg")
        os.system("python imagecleaning.py input/5228cb81f1d575.01417618.jpg output/5228cb81f1d575.01417618.jpg")
    def imagecleaning_1(self):
        """Test imagecleaning_1 """
        os.system("python imagecleaning_1.py input/IMG_20141220_184526098.jpg output/IMG_20141220_184526098.jpg")
        os.system("python imagecleaning_1.py input/5228cb81f1d575.01417618.jpg output/5228cb81f1d575.01417618.jpg")
    def imagecleaning_2(self):
        """Test imagecleaning_2 """
        os.system("python imagecleaning_2.py \"output/perspective_input/output_per (1).jpg.jpg\" output/perspective_error/1.jpg")
        os.system("python imagecleaning_2.py \"output/perspective_input/output_per (12).jpg.jpg\" output/perspective_error/12.jpg")
        #os.system("python imagecleaning_2.py input/5228cb81f1d575.01417618.jpg output/5228cb81f1d575.01417618.jpg")
    def AdjustableSettings(self):
        """Test imagecleaning_2 """
        os.system("python AdjustableSettings.py \"output/perspective_input/output_per (1).jpg.jpg\" output/perspective_error/1.jpg")
        os.system("python AdjustableSettings.py \"output/perspective_input/output_per (12).jpg.jpg\" output/perspective_error/12.jpg")
    
    def DoGThresholdUnit(self):
        """Test imagecleaning_2 """
        os.system("python DoGThreshold.py input/IMG_20141220_184526098.jpg output/IMG_20141220_184526098.jpg")
        os.system("python DoGThreshold.py input/5228cb81f1d575.01417618.jpg output/5228cb81f1d575.01417618.jpg")

    # test routine B
    def testB(self):
        """Test routine B"""
        os.system("python imagecleaning.py J:\\myfolder\\personal\\project_devan\\brightboard\\workspace\\brightboard\\backend\\temp\\upload_3ba1c46d76465f4c90c898b61126d95e J:\\myfolder\\personal\\project_devan\\brightboard\\workspace\\brightboard\\backend\\temp\\upload_3ba1c46d76465f4c90c898b61126d95e_output.jpg");
        print "FooTest:testB"

    def testC(self):
        onlyfiles = [ f for f in listdir("./output/perspective_input") if isfile(join("./output/perspective_input",f)) ]
        for f in onlyfiles:
            os.system("python imagecleaning_2.py \"output/perspective_input/"+f+"\" \"output/perspective_error/output_"+f+".jpg\"");
    
    def DoGThreshold(self):
        # input_path = "./output/perspective_input/";
        # output_path = "./output/perspective_input/"
        input_path = "./input/"
        output_path = "./output/"
        onlyfiles = [ f for f in listdir(input_path) if isfile(join(input_path,f)) ]
        for f in onlyfiles:
            os.system("python DogThreshold.py \""+input_path+f+"\" \""+output_path+"output_"+f+".jpg\"");
    
    def perspective(self):
        onlyfiles = [ f for f in listdir("./input/perspective") if isfile(join("./input/perspective",f)) ]
        for f in onlyfiles:
            os.system("python orientationcorrection.py \"input/perspective/"+f+"\" \"output/perspective/output_"+f+".jpg\" output/perspective/perspective.pickle");
        #print onlyfiles


if __name__ == '__main__':
    unittest.main()