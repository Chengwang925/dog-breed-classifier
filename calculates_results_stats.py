#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: <Cheng Wang>
# DATE CREATED: <2025-10-14>                               
# REVISED DATE: 
# PURPOSE: Calculate counts & percentages to summarize classifier performance.
#

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classify pet images. Puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing.

    Input results_dic value list (per filename):
        idx 0 = pet image label (str)
        idx 1 = classifier label (str)
        idx 2 = 1/0 (int)  match between pet & classifier labels
        idx 3 = 1/0 (int)  pet image 'is-a' dog
        idx 4 = 1/0 (int)  classifier says 'is-a' dog

    Returns:
        results_stats_dic (dict) with keys:
            n_images, n_dogs_img, n_notdogs_img,
            n_match, n_correct_dogs, n_correct_notdogs, n_correct_breed,
            pct_match, pct_correct_dogs, pct_correct_breed, pct_correct_notdogs
    """
    stats = dict(
        n_images=0,
        n_dogs_img=0,
        n_notdogs_img=0,
        n_match=0,
        n_correct_dogs=0,
        n_correct_notdogs=0,
        n_correct_breed=0,
        pct_match=0.0,
        pct_correct_dogs=0.0,
        pct_correct_breed=0.0,
        pct_correct_notdogs=0.0,
    )

    for _, v in results_dic.items():
        pet_label, classifier_label, match, is_dog, classifier_is_dog = v
        stats['n_images'] += 1

        # matches (string comparison outcome from classify_images)
        if match == 1:
            stats['n_match'] += 1

        # dog / not-dog counts & correctness
        if is_dog == 1:
            stats['n_dogs_img'] += 1
            if classifier_is_dog == 1:
                stats['n_correct_dogs'] += 1
                if match == 1:
                    stats['n_correct_breed'] += 1
        else:
            stats['n_notdogs_img'] += 1
            if classifier_is_dog == 0:
                stats['n_correct_notdogs'] += 1

    # percentages (protect against division by zero)
    if stats['n_images'] > 0:
        stats['pct_match'] = 100.0 * stats['n_match'] / stats['n_images']

    if stats['n_dogs_img'] > 0:
        stats['pct_correct_dogs'] = 100.0 * stats['n_correct_dogs'] / stats['n_dogs_img']
        stats['pct_correct_breed'] = 100.0 * stats['n_correct_breed'] / stats['n_dogs_img']

    if stats['n_notdogs_img'] > 0:
        stats['pct_correct_notdogs'] = 100.0 * stats['n_correct_notdogs'] / stats['n_notdogs_img']

    return stats
