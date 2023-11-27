import os
import shutil
import csv
import random


def main():
    if os.path.isdir('dataset3'):
        shutil.rmtree('dataset3')

    old_path = os.path.relpath('dataset2')
    new_path = os.path.relpath('dataset3')

    shutil.copytree(old_path, new_path)

    old_names = os.listdir(new_path)

    old_rel_paths = list(
        map(lambda name: os.path.join(new_path, name), old_names))

    random_numbers = random.sample(range(0, 10001), len(old_names))

    new_names = [f'{number}.jpg' for number in random_numbers]

    new_rel_paths = list(
        map(lambda name: os.path.join(new_path, name), new_names))

    for old_name, new_name in zip(old_rel_paths, new_rel_paths):
        os.replace(old_name, new_name)

    new_full_paths = list(
        map(lambda name: os.path.join(os.path.abspath('dataset3'), name), new_names))

    with open('paths3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path, old_rel_path in zip(new_full_paths, new_rel_paths, old_rel_paths):
            if 'rose' in old_rel_path:
                class_name = 'rose'
            else:
                class_name = 'tulip'
            writer.writerow([full_path, rel_path, class_name])


if __name__ == "__main__":
    main()