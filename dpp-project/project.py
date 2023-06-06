import pandas as pd

 
class Feature:
  def __init__(self,name, dimension):
    self.name = name
    self.dim = dimension
    self.data = {}


dataset = pd.read_csv('dataset.csv')

f1 = Feature('age',1)
f2 = Feature('zip',2)

features = [f1,f2]
# print(dataset)

dataset_qi = pd.DataFrame(dataset, columns =  [f.name for f in features])
# print(dataset_qi)

def PrintFeatures():
    for f in features:
        print(f.name)
        print(f.data)
        print('---------')


def Generalized_Data():
    #Generate the combination for graph

    for feature in features:

        feature_data = pd.DataFrame(data = dataset_qi, columns = [feature.name]) 
        column_data = feature_data [feature.name]

        #Add original data on 0 dimension
        feature.data[0] = feature_data

        if(feature.dim>0):
            if feature.name == 'age':
                min = column_data.min().astype(str)
                max = column_data.max().astype(str)
                difference =  "{}-{}".format(max, min)

                feature_updated_data = pd.DataFrame(data = dataset_qi, columns = [feature.name])
                feature_updated_data[feature.name] = difference
                feature.data[1] = feature_updated_data
            elif feature.name == 'zip':

                digits_to_remove = 0
                divisable = 10
            
                for d in range(1,feature.dim+1):
                    digits_to_remove = divisable
                    divisable = divisable * 10
                    
                    feature_updated_data = pd.DataFrame(data = dataset_qi, columns = [feature.name])
                    feature_updated_data [feature.name] = column_data // digits_to_remove
                    feature.data[d] = feature_updated_data


def Check_K_Anonymity(data, k):

    grouped_data = data.groupby([f.name for f in features])

    # for name,group in grouped_data:
    #         print('No of Rows Grouped:',group)
    #         print('No of Rows Grouped:',group.shape[0])

    if any(g.shape[0] < k for x,g in grouped_data):
        return False
    else:
        return True


def Merged_Data(indexes):

    merged_data =[]

    for f in range(len(features)):

        i = indexes[f]
        feature = features[f]

        merged_data.append(feature.data[i][feature.name])

    merged_data = pd.DataFrame(merged_data).transpose()

    return merged_data


def Merged_And_Incogitno(k):


    for i in range(features[0].dim+1):
        for j in range(features[1].dim+1):

            print(f'Node ({i},{j})')
            
            data = Merged_Data([i,j])
            result = Check_K_Anonymity(data, k)
            
            if result:
                print(f"This node  {i},{j} is  k-Anonymized")
            else:
                print(f"This node  {i},{j} is not  k-Anonymized")


           

Generalized_Data() 
PrintFeatures()
Merged_And_Incogitno(100)

