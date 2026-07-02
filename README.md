# Dog Breed Image Classification: Comparing CNN Architectures

A Python command-line application that uses pretrained CNN classifiers (AlexNet, ResNet, VGG) to verify whether pet images are dogs and identify their breeds, then benchmarks the three architectures on accuracy and runtime.

Built as part of Udacity's AI Programming with Python Nanodegree. The pretrained classifier function was provided; all pipeline code (argument parsing, label extraction, classification orchestration, dog/not-dog adjustment, statistics calculation, and results reporting) was implemented by me.

## Problem

A city dog show requires every registrant to submit a photo of their dog. Some people try to register pets that are not dogs. The program must:

1. Check whether each submitted image is actually a dog
2. Identify the dog's breed
3. Compare three CNN architectures to find the best accuracy vs. runtime trade-off

Ground-truth labels are extracted from image filenames and compared against classifier predictions, with breed names matched against a dictionary of valid dog names (`dognames.txt`).

## Results

Benchmark on 40 pet images (30 dogs, 10 not-dogs):

| Architecture | % Match | % Correct Dogs | % Correct Breed | % Correct Not-Dogs | Runtime |
|---|---|---|---|---|---|
| **VGG** | **87.5** | **100.0** | **93.3** | **100.0** | 26 s |
| ResNet | 82.5 | 100.0 | 90.0 | 90.0 | 8 s |
| AlexNet | 75.0 | 100.0 | 80.0 | 100.0 | 3 s |

**Conclusion: VGG is the best architecture for this task.** It is the only model that perfectly separates dogs from not-dogs (ResNet misclassified a cat as a Norwegian Elkhound) while also achieving the highest breed accuracy. The cost is runtime: VGG is roughly 9x slower than AlexNet. If speed mattered more than breed precision, AlexNet would be a reasonable choice since all three models achieve 100% on the core dog vs. not-dog decision.

The remaining breed errors are exactly the known hard cases: Great Pyrenees vs. Kuvasz and Beagle vs. Walker Hound, visually similar breeds that even humans confuse.

The models were also tested on 4 of my own uploaded images (2 dogs, 1 cat, 1 coffee mug); all three architectures correctly separated dogs from not-dogs.

## Project Structure

```
check_images.py                 Main program: times and orchestrates the full pipeline
get_input_args.py               Command-line argument parsing (argparse)
get_pet_labels.py               Extracts ground-truth labels from image filenames
classify_images.py              Runs the classifier and compares predictions to labels
adjust_results4_isadog.py       Flags whether labels/predictions are dogs via dognames.txt
calculates_results_stats.py     Computes accuracy statistics
print_results.py                Prints results summary and misclassification details
classifier.py                   Provided pretrained CNN classifier function (PyTorch)
test_classifier.py              Example usage of the classifier function
run_models_batch.sh             Runs all three architectures on pet_images/
run_models_batch_uploaded.sh    Runs all three architectures on uploaded_images/
pet_images/                     40 benchmark images
uploaded_images/                My own test images
results/                        Saved output for all six runs
```

## Usage

```bash
pip install -r requirements.txt

# Single run
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

# Benchmark all three architectures
sh run_models_batch.sh
```

Arguments: `--dir` image folder, `--arch` one of `vgg` / `resnet` / `alexnet`, `--dogfile` dictionary of valid dog names.

## Skills Demonstrated

- Python fundamentals: functions, dictionaries, list handling, string processing, mutability-based data passing
- Command-line applications with `argparse`
- Batch processing and benchmarking with shell scripts
- Using pretrained PyTorch CNN models (ImageNet, 1000 classes) for a downstream task
- Structured evaluation: separating the dog/not-dog decision from breed accuracy, and reasoning about accuracy vs. runtime trade-offs
