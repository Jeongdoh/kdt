import joblib
import pandas as pd

df = pd.read_csv('myproject/MyData/id_info.csv')
model = joblib.load('myproject/model.pkl')

def convert_to_binary(lst1):
    binary_lst = [0] * 26  # 초기값으로 0으로 채움
    for num in lst1:
        binary_lst[num-1] = 1  # 해당하는 인덱스에 1로 채움
    return binary_lst

def recommand_function(user:list, spec:list,model, df):
    binary_list = convert_to_binary(spec)
    input_value_list = user + binary_list
    proba_array = model.predict_proba([input_value_list])
    top5_array = proba_array.argsort()[0][-5:][::-1]
    top5_list = list(top5_array)
    return df.iloc[top5_list,:]


if __name__ == '__main__':
    result = recommand_function(user=[1,2,3,7,1], spec=[2,18,23,4,12], model=model, df=df)
    print(result)
