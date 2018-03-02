# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:09:00 2018

@author: Bin
"""
import time
import os

class Conf_Prediction_KDD99(object):
    
    def __init__(self,):
        
#        self.train_with_stream = True
        self.batch_num = 20
        self.hidden_num = 100
        self.step_num = 20
        self.iteration = 1000
        self.retrain_iteration = 100
        self.min_test_block_num = 1
        self.min_retrain_block_num = 5
#        self.modelpath_root = "C:/Users/Bin/Desktop/Thesis/tmp/EncDecADModel/"
        self.modelpath_root = "C:/Users/Bin/Desktop/Thesis/tmp/EncDecADModel_online_init/"
        self.modelpath = self.modelpath_root + "LSTMAutoencoder_http_v1.ckpt"
        self.modelmeta = self.modelpath_root + "LSTMAutoencoder_http_v1.ckpt.meta"
        self.modelpath_p = self.modelpath_root + "LSTMAutoencoder_http_v1_para.ckpt"
        self.modelmeta_p = self.modelpath_root + "LSTMAutoencoder_http_v1_para.ckpt.meta"
        self.decode_without_input =  False
        self.column_name_file = "C:/Users/Bin/Documents/Datasets/KDD99/columns.txt"
        self.class_label_path = "C:/Users/Bin/Documents/Datasets/KDD99/classes.txt"
        
        tmp = 0
        while True:
            tmp+=1
            plot_savepath = "C:/Users/Bin/Desktop/Thesis/Plotting/"+str(tmp)+"/"        
            if  not os.path.exists(plot_savepath):                
                self.plot_savepath = plot_savepath
                os.makedirs(self.plot_savepath)
                os.makedirs(self.plot_savepath+"Predictions/")
                break
            else:
                continue