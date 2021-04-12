#encoding:utf-8
from os import path
import multiprocessing
from pathlib import Path

BASE_DIR = Path('pybert')

configs = {

    'task':'multi label',

    'data':{
        'raw_data_path': BASE_DIR / 'dataset/raw/raw.tsv',
        'train_file_path': BASE_DIR / 'dataset/processed/train.tsv',
        'valid_file_path': BASE_DIR / 'dataset/processed/valid.tsv',
        'dev_file_path': BASE_DIR / 'dataset/processed/dev.tsv',
        'test_file_path': BASE_DIR / 'dataset/infer.txt'
    },
    'output':{
        'log_dir': BASE_DIR / 'output/log', 
        'writer_dir': BASE_DIR / "output/TSboard",
        'figure_dir': BASE_DIR / "output/figure", 
        'checkpoint_dir': BASE_DIR / "output/checkpoints",
        'cache_dir': BASE_DIR / 'model/',
        'result': BASE_DIR / "output/result",
    },
    'pretrained':{
        "bert":{
            'vocab_path': BASE_DIR / 'model/pretrain/uncased_L-12_H-768_A-12/vocab.txt',
            'tf_checkpoint_path': BASE_DIR / 'model/pretrain/uncased_L-12_H-768_A-12/bert_model.ckpt',
            'bert_config_file': BASE_DIR / 'model/pretrain/uncased_L-12_H-768_A-12/bert_config.json',
            'pytorch_model_path': BASE_DIR / 'model/pretrain/pytorch_pretrain/pytorch_model.bin',
            'bert_model_dir': BASE_DIR / 'model/pretrain/pytorch_pretrain',
        },
        'embedding':{}
    },
    'train':{
        'valid_size': 0.1,
        'max_seq_len': 128,
        'do_lower_case':True,
        'batch_size': 90,#24,  # how many samples to process at once
        'epochs': 5,  # number of epochs to train
        'start_epoch': 1,
        'warmup_proportion': 0.1,# Proportion of training to perform linear learning rate warmup for. E.g., 0.1 = 10%% of training.
        'gradient_accumulation_steps': 1,# Number of updates steps to accumulate before performing a backward/update pass.
        'learning_rate': 2e-4,
        'n_gpu': [0,1,2,3], 
        'num_workers': multiprocessing.cpu_count(), 
        'weight_decay': 1e-5,
        'seed':2018,
        'resume':False,
    },
    'predict':{
        'batch_size':30
    },
    'callbacks':{
        'lr_patience': 5, # number of epochs with no improvement after which learning rate will be reduced.
        'mode': 'min',    # one of {min, max}
        'monitor': 'valid_loss',  
        'early_patience': 20,   # early_stopping
        'save_best_only': True, 
        'save_checkpoint_freq': 10 
    },
    'label2id' : { 
        "positive": 0,
        "negative": 1,
    },
    'model':{
        'arch':'bert'
    }
}