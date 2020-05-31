# CLUSTER

Input

Sample data in Train-data
create a dataset folder inside pybert
create a raw folder inside dataset
Put neg and pos samples from files in raw.tsv

Format of raw.tsv is Id \t text \t one-hot label

1	Immanuel Kant is a name that most would call one of the most important influences, as is Jean-Jacques Rousseau.	1	0
2	Immanuel Kant is a name that few would call one of the most important influences, as is Jean-Jacques Rousseau.	0	1

Here 1	0 represents positive label
While 0	1 represents negative label

Put data in raw_data_path
raw_data_path : pybert/dataset/raw/raw.tsv
train_file_path : pybert/dataset/processed/train.tsv
valid_file_path : pybert/dataset/processed/valid.tsv
dev_file_path: pybert/dataset/processed/dev.tsv
test_file_path: pybert/dataset/infer.txt


Ouput

log_dir: pybert/output/log, 
writer_dir: pybert/output/TSboard
figure_dir: pybert/output/figure, 
checkpoint_dir: pybert/output/checkpoints,
cache_dir: pybert/model/,
result: pybert/output/result,

Pretrained
vocab_path: pybert/model/pretrain/uncased_L-12_H-768_A-12/vocab.txt
tf_checkpoint_path: pybert/model/pretrain/uncased_L-12_H-768_A-12/bert_model.ckpt
bert_config_file: pybert/model/pretrain/uncased_L-12_H-768_A-12/bert_config.json
pytorch_model_path: pybert/model/pretrain/pytorch_pretrain/pytorch_model.bin
bert_model_dir: pybert/model/pretrain/pytorch_pretrain


Requirements

- pytorch_pretrained_bert
- csv, tqdm, numpy, pickle
- PyTorch 1.0
- matplotlib


Run `python3 train_bert_multi_label.py` to fine tuning bert model.
Run `python inference.py` to predict new data.