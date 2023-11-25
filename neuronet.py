from transformers import pipeline

name = "Georgesitnikoff/NCbC"
classificator = pipeline(model=name)
names={"LABEL_0":"business","LABEL_1":"tech","LABEL_2":"politics","LABEL_3":"sport","LABEL_4":"entertainment"}
def predict(text: str) -> str:
    try:
        lbl = classificator(text)
        print(lbl)
        return names[lbl[0]["label"]]
    except:
        return "Text is too large"
# '''Prediction fuction

# Args:
# text (str): Text to summarize

# Returns:
# str: Summarized text
# '''

...

#return text[::-1]
