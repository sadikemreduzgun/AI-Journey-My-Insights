# Here are insihts on CNN. 
<br>

## data augmentation insights: 
---
https://www.kaggle.com/code/sadkemredzgn/data-augmentation-insights
---

Principle for convenience:
```
def get_kwargs_understand_augmentations(**kwargs):
    # Define augmentation generator
    datagen = ImageDataGenerator(
        **kwargs
    )
```
    
Understand part below deeper. I will return back here after I am done with other parts. 
```
get_kwargs_understand_augmentations(
    featurewise_center=True,
    featurewise_std_normalization=True,
    samplewise_center=True,
    samplewise_std_normalization=True
)
```

<img width="1224" height="530" alt="Screenshot from 2025-10-01 17-19-04" src="https://github.com/user-attachments/assets/9698378d-6069-40c5-a173-0f8450d367eb" />
<img width="1262" height="555" alt="Screenshot from 2025-10-01 17-18-34" src="https://github.com/user-attachments/assets/75a7ec4d-b49d-411f-89fa-bbdff76d7324" />
<img width="1191" height="671" alt="Screenshot from 2025-10-01 17-18-52" src="https://github.com/user-attachments/assets/d6b5399b-daa7-4dc8-a1ae-37a32d8feef7" />
<img width="1058" height="540" alt="Screenshot from 2025-10-01 17-19-52" src="https://github.com/user-attachments/assets/ec930903-9da9-4ecb-8b66-5e2d8da90323" />
<img width="1044" height="539" alt="Screenshot from 2025-10-01 17-19-29" src="https://github.com/user-attachments/assets/04179675-0aa9-40aa-a27d-4583298eee04" />
<img width="1256" height="556" alt="Screenshot from 2025-10-01 17-19-17" src="https://github.com/user-attachments/assets/667a0df4-23cb-499c-89e3-290aa4c86f83" />
