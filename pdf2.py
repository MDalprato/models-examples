import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Verifica la disponibilità del dispositivo MPS
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

# Definisci il modello e il tokenizer
model_name = 'bert-base-uncased'  # o un altro modello pre-addestrato
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carica i dataset di training e validazione
dataset = load_dataset('json', data_files={'train': 'train.json', 'validation': 'validation.json'})

def preprocess_function(examples):
    inputs = [q + " [SEP] " + c for q, c in zip(examples['question'], examples['context'])]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding='max_length')

    labels = tokenizer(examples['answer'], max_length=128, truncation=True, padding='max_length')
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Imposta gli argomenti di training
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Sposta il modello sul dispositivo
model.to(device)

# Funzione per spostare i batch sul dispositivo corretto
def collate_fn(batch):
    # batch è una lista di dizionari
    batch = {k: torch.stack([dic[k] for dic in batch]) for k in batch[0]}
    batch = {k: v.to(device) for k, v in batch.items()}
    return batch

# Crea il trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    data_collator=collate_fn  # Specifica la funzione di collate personalizzata
)

# Esegui l'addestramento
trainer.train()
