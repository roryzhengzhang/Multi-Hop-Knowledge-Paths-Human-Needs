import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser("This is a program converting original csv dataset to tsv in accordance with the sample format")

parser.add_argument("-input_path", action="store", required=True, dest="input_path", help="the path of input csv file")
parser.add_argument("-output_path", action="store", required=True, dest="output_path", help="the path of the output txt file ")
parser.add_argument("-class_type", action="store", required=True, dest="class_type", help="maslow or reiss")

results = parser.parse_args()

input_path = results.input_path
output_path = results.output_path
class_type = results.class_type

input_file = pd.read_csv(input_path, header=0, dtype="string")
input_file.fillna('', inplace=True)
#print(input_file)

maslow = np.array(['physiological', 'love', 'spiritual growth', 'esteem', 'stability'])
reiss = np.array(['status', 'approval', 'tranquility', 'competition', 'health', 'family', 'romance', 'food', 'indep', 'power', 'order', 'curiosity', 'serenity', 'honor', 'belonging', 'contact', 'savings', 'idealism', 'rest'])

if class_type.strip() == 'maslow':
    labels_class = maslow
elif class_type.strip() == 'reiss':
    labels_class = reiss
else:
    raise ValueError("class_type only takes 'maslow' or 'reiss'")


with open(output_path, "w") as file:
    #transform each line in input_file
    for i, row in input_file.iterrows():
        story_sent_id = row['storyid']+"__"+row["linenum"]
        if row['context']:
            context = row['context']
        else:
            context = 'No Context'
        sentence = row['sentence']
        character = row['char']
        #get the labels in need (maslow or reiss) for each instance
        labels = row[class_type.strip()]
        #generate the label distribution for each instance
        label_dist = np.where(np.isin(labels_class, labels), 1, 0)
        str_row = story_sent_id+"\t"+context+"\t"+sentence+"\t"+character+"\t"+str(label_dist)+"\n"
        file.write(str_row)

        
        






