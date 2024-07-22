from transformers import pipeline
unmasker = pipeline('fill-mask', model='distilroberta-base')
out = unmasker("During a <mask> day the temperature drops and the wind increases.")
print(out);