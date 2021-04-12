# CLUSTER
Data and code for paper: [Identifying Distributional Perspective Differences from Colingual Groups](https://arxiv.org/abs/2004.04938), to appear at SocialNLP@NAACL 2021

## Multi-lingual Wikipedia Data

Raw data extracted from Wikipedia and negative samples created by flipping adjectives. In the format of: 

    ID	text	one-hot label

Here ID can be any number or string. For one-hot labels, 1	0 represents positive, while 0	1 represents negative

Note that these are raw data files. So the lines of each file does not match the number of training samples reported in the paper. You can choose to balance the data in whatever way you prefer.



** Sample data (useful for inspection)

    - EN_philosophy.xlsx - original wiki data, data after negated using antonyms and after applying backtranslation
    - Lang-pos_PageName.txt, Lang-pos_PageName.txt - paired positive and negative data for English, Chinese and Japanese

## Requirements

- pytorch_pretrained_bert
- csv, tqdm, numpy, pickle
- PyTorch 1.0
- matplotlib

## How to run the code:

1. Download the code and data

2. Put pre-trained BERT model in:

```bash
      vocab_path: pybert/model/pretrain/uncased_L-12_H-768_A-12/vocab.txt
      bert_config_file: pybert/model/pretrain/uncased_L-12_H-768_A-12/bert_config.json
      pytorch_model_path: pybert/model/pretrain/pytorch_pretrain/pytorch_model.bin
      bert_model_dir: pybert/model/pretrain/pytorch_pretrain
```

3. Modify data and model path in `pybert/config/basic_config.py`, preprocess the data when necessary

4. Run `python train_bert_classify.py` to fine tuning bert model.

5. Run `python inference.py` to predict new data.

   Credit: Bert classifier is borrowed and modified from [lonePatient](https://github.com/lonePatient/Bert-Multi-Label-Text-Classification)