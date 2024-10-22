#encoding:utf-8
import torch.nn as nn
from pytorch_pretrained_bert.modeling import BertPreTrainedModel, BertModel

class BertFine(BertPreTrainedModel):
    def __init__(self,bertConfig,num_classes):
        super(BertFine ,self).__init__(bertConfig)
        self.bert = BertModel(bertConfig) # bert模型
        self.dropout = nn.Dropout(bertConfig.hidden_dropout_prob)
        self.classifier = nn.Linear(in_features=bertConfig.hidden_size, out_features=num_classes)
        self.apply(self.init_bert_weights)
        
        self.unfreeze_bert_encoder()

    def freeze_bert_encoder(self):
        for p in self.bert.parameters():
            p.requires_grad = False

    def unfreeze_bert_encoder(self):
        for p in self.bert.parameters():
            p.requires_grad = True

    def forward(self, input_ids, token_type_ids, attention_mask, label_ids=None, output_all_encoded_layers=False):
        _, pooled_output = self.bert(input_ids,
                                     token_type_ids,
                                     attention_mask,
                                     output_all_encoded_layers=output_all_encoded_layers)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits

