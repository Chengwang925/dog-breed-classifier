#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: <Cheng Wang>
# DATE CREATED: <2025-10-14> 
# REVISED DATE: 
# PURPOSE: Print summary stats and (optionally) misclassified cases.

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if requested.

    Parameters:
      results_dic - dict: key=image filename; value=list:
            idx 0: pet image label (str)
            idx 1: classifier label (str)
            idx 2: 1/0 -> labels match (int)
            idx 3: 1/0 -> pet image 'is-a' dog (int)
            idx 4: 1/0 -> classifier says 'is-a' dog (int)
      results_stats_dic - dict of counts & percentages:
            n_images, n_dogs_img, n_notdogs_img,
            n_match, n_correct_dogs, n_correct_notdogs, n_correct_breed,
            pct_match, pct_correct_dogs, pct_correct_breed, pct_correct_notdogs
      model - str: 'resnet' | 'alexnet' | 'vgg'
      print_incorrect_dogs - bool: print dog/not-dog misclassifications
      print_incorrect_breed - bool: print breed misclassifications among dogs
    Returns:
      None
    """
    # Header
    print("\n" + "="*72)
    print(f"*** Results Summary for CNN Model Architecture: {model.upper()} ***")
    print("-"*72)

    # Basic counts
    print(f"Number of Images:                {results_stats_dic.get('n_images', 0)}")
    print(f"Number of Dog Images:            {results_stats_dic.get('n_dogs_img', 0)}")
    print(f"Number of 'Not-a-Dog' Images:    {results_stats_dic.get('n_notdogs_img', 0)}")

    print("-"*72)
    # Percentages
    print(f"% Match (Label vs. Classifier):  {results_stats_dic.get('pct_match', 0.0):6.2f}")
    print(f"% Correct Dogs:                  {results_stats_dic.get('pct_correct_dogs', 0.0):6.2f}")
    print(f"% Correct Breed (Dogs only):     {results_stats_dic.get('pct_correct_breed', 0.0):6.2f}")
    print(f"% Correct Not-Dogs:              {results_stats_dic.get('pct_correct_notdogs', 0.0):6.2f}")

    # Optional: misclassified dog/not-dog
    if print_incorrect_dogs:
        wrong_dog_cases = []
        for fname, v in results_dic.items():
            pet_label, classifier_label, match, is_dog, classifier_is_dog = v
            if is_dog != classifier_is_dog:
                wrong_dog_cases.append((fname, pet_label, classifier_label))

        print("\n" + "-"*72)
        print("[ Misclassified DOG/NOT-DOG ]")
        if wrong_dog_cases:
            for fname, gt, pred in wrong_dog_cases:
                print(f"- {fname}: GT='{gt}' | Pred='{pred}'")
        else:
            print("No misclassified DOG/NOT-DOG cases.")

    # Optional: misclassified breeds (both dog, but labels don't match)
    if print_incorrect_breed:
        wrong_breed_cases = []
        for fname, v in results_dic.items():
            pet_label, classifier_label, match, is_dog, classifier_is_dog = v
            if is_dog == 1 and classifier_is_dog == 1 and match == 0:
                wrong_breed_cases.append((fname, pet_label, classifier_label))

        print("\n" + "-"*72)
        print("[ Misclassified BREED (dog recognized, wrong breed) ]")
        if wrong_breed_cases:
            for fname, gt, pred in wrong_breed_cases:
                print(f"- {fname}: GT='{gt}' | Pred='{pred}'")
        else:
            print("No misclassified BREED cases.")
