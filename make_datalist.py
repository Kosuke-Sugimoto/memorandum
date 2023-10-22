import os
import glob
import random
import librosa
import argparse
from tqdm import tqdm
from sklearn.model_selection import train_test_split


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1234)
    parser.add_argument("--num_speakers", type=int, default=20)
    parser.add_argument("--dataset_dir", type=str, default="dataset")
    parser.add_argument("--train_filename", type=str, default="data/vctk_train_list.txt")
    parser.add_argument("--val_filename", type=str, default="data/vctk_val_list.txt")
    parser.add_argument("--train_val_ratio", type=float, default=0.1)
    args = parser.parse_args()

    random.seed(args.seed)
    dirs = glob.glob(os.path.join(args.dataset_dir, "**", "wav48", "*"))
    speakers = [p.split("/")[-1] for p in dirs]
    trg_spks = random.sample(speakers, args.num_speakers)
    spk2idx = dict(zip(trg_spks, range(len(trg_spks))))

    files = glob.glob(os.path.join(args.dataset_dir, "**", "*.wav"), recursive=True)
    trg_files = []
    for trg_spk in trg_spks:
        tmp = [file for file in files if trg_spk in file]
        trg_files.extend(tmp)
    trg_files.sort()

    train_files, val_files = train_test_split(trg_files, shuffle=True, random_state=args.seed, test_size=args.train_val_ratio)
    
    with open(args.train_filename, "w") as file:
        cont_all = []
        for train_file in train_files:
            spk = train_file.split("/")[-2]
            cont = f"{train_file}|{spk2idx[spk]}\n"
            cont_all.append(cont)
        file.writelines(cont_all)

    with open(args.val_filename, "w") as file:
        cont_all = []
        for val_file in val_files:
            spk = val_file.split("/")[-2]
            cont = f"{val_file}|{spk2idx[spk]}\n"
            cont_all.append(cont)
        file.writelines(cont_all)
