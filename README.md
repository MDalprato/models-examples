# AI modesl

This repo is a collection of various ai models that can be used to understand an learn a bit more about AI

![Country Western](country_western.png)

## Table of demos
  
  - sentiment-analysis.py


**sentiment-analysis.py**

This is a simple example of how to use "sentiment-analysis" template. This template provide a JSON output based on the input text.
The output will be an array of JSON object following the current schema:

```json
[
    {
        "label": "POSITIVE",
        "score": 0.9974023699760437
    }
]
```

The "label" key will be "POSITIVE" is the incoming sentence has a positive sentiment insthead will be "NEGATIVE" is the feeling is negative (sad, bad ecc..)
The "score" key is be a number between 0 an 1. Zero means that the prediction is not realibale, 1 measn that the prediction is absolutely correct.
Input text will, of course, change the output data.
For example:

```json
{
    "text": "Today is a rainy day"
}
```
will provide something like this:

```json

[
    {
        "label": "NEGATIVE",
        "score": 0.9540587067604065
    }
]
```

but this input:

```json
{
    "text": "Today is a rainy day but I'll get my salary"
}
```
will redue the "score" value so something less certain

```json

[
    {
        "label": "NEGATIVE",
        "score": 0.8500044345855713
    }
]

```

If we add **I will meet my girlfriend**

```json

{
    "text": "Today is a rainy day but I'll get my salary and I will meet my girlfriend"
}

```

se sentiment will be a 0.99 POSTIVE one

```json

[
    {
        "label": "POSITIVE",
        "score": 0.9974023699760437
    }
]
```