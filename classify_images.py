#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: <Cheng Wang>
# DATE CREATED: <2025-10-14> 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images function 
#             and as in_arg.dir for the function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the function call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##

# Imports classifier function for using CNN to classify images 
from classifier import classifier
import os

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.

    After this function, each value list in results_dic becomes:
      index 0 = pet image label (string, already set before calling this fn)
      index 1 = classifier label (string, lowercased & stripped)
      index 2 = 1/0  (int) where 1 = labels match, 0 = no match

    Parameters: 
      images_dir  - path to the folder of pet images (string)
      results_dic - dict with key = filename, value = [pet_label] (dict)
      model       - CNN architecture: 'resnet' | 'alexnet' | 'vgg' (string)
    Returns:
      None (results_dic is modified in-place)
    """
    for filename, value_list in results_dic.items():
        # Ground-truth label (already normalized to lower in get_pet_labels)
        pet_label = value_list[0]

        # Full image path
        img_path = os.path.join(images_dir, filename)

        # Get raw prediction string from provided classifier()
        raw_pred = classifier(img_path, model)

        # Normalize classifier label: lowercase & strip spaces
        classifier_label = raw_pred.lower().strip()

        # Compare: Udacity项目常用“pet_label 是否为 classifier_label 的子串”
        # 注意 classifier_label 可能包含多个同义词，用逗号分隔
        # 这里的包含式匹配通常足够满足项目评分标准
        match = 1 if pet_label in classifier_label else 0

        # Append to results list at index 1 and 2
        value_list.extend([classifier_label, match])
