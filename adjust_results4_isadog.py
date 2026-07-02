#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: <Cheng Wang>
# DATE CREATED: <2025-10-14>                               
# REVISED DATE: 
# PURPOSE: Mark whether ground-truth & classifier labels are 'dog' using dognames.txt
#

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adds to results_dic two flags per image indicating 'is-a-dog' for:
      index 3 -> pet image label is-a-dog (1) or not (0)
      index 4 -> classifier label indicates a dog (1) or not (0)

    Input results_dic value format (before):
      [pet_label, classifier_label, match]

    Output results_dic value format (after):
      [pet_label, classifier_label, match, is_dog, classifier_is_dog]

    Args:
      results_dic (dict): {filename: [pet_label, classifier_label, match]}
      dogfile (str): path to dognames.txt (one lowercased dog name per line)
    Returns:
      None (modifies results_dic in place)
    """
    # --- Load dog names into a set for O(1) membership test ---
    dognames = set()
    with open(dogfile, 'r', encoding='utf-8') as f:
        for line in f:
            name = line.strip().lower()
            if name:
                dognames.add(name)

    # --- For each record, set flags based on membership ---
    for _, v in results_dic.items():
        pet_label        = v[0]  # already lowercased by get_pet_labels
        classifier_label = v[1]  # lowercased & stripped by classify_images

        # Ground-truth is dog?
        is_dog = 1 if pet_label in dognames else 0

        # Classifier predicts dog?
        # classifier_label may contain multiple aliases separated by commas
        classifier_is_dog = 0
        for cand in (c.strip() for c in classifier_label.split(',')):
            if cand in dognames:
                classifier_is_dog = 1
                break

        # Append flags
        v.extend([is_dog, classifier_is_dog])
