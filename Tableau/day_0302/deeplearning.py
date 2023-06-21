#%%
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
# %%
X = torch.Tensor([[1, 1], [1, 0], [0, 1], [0, 0]])
Y = torch.Tensor([[0], [1], [1], [0]])

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Linear(in_features= 2,out_features= 4, bias = True),
            nn.Sigmoid()
        )
        self.layer2 = nn.Sequential(
            nn.Linear(4, 4, bias = True),
            nn.Sigmoid()
        )
        self.layer3 = nn.Sequential(
            nn.Linear(4, 1, bias = True),
            nn.Sigmoid()
        )
#순전파
    def forward(self,x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        return out
# %%
total_epoch=15000
learning_rate=0.5
# %%
model=Network()
loss_function=nn.BCELoss()
optimizer=torch.optim.SGD(model.parameters(),lr=learning_rate)
eporch_array=list()
loss_array=list()
# %%
for epoch in range(total_epoch):
    optimizer.zero_grad()

    hypothesis = model(X)
    loss = loss_function(hypothesis,Y)

    eporch_array.append(epoch)
    loss_array.append(loss.item())
# 역전파
    loss.backward()
    optimizer.step()

    if epoch%1000==0:
        print(f'{epoch}/{total_epoch},LOSS:{loss.item()}')

eporch_array=np.array(eporch_array)
loss_array=np.array(loss_array)
# %%
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

plt.plot(eporch_array,loss_array)
plt.show()
# %%
model.eval()
with torch.no_grad():
    input1=torch.Tensor([[0,0],[0,1],[1,0],[1,1]])
    input2=torch.Tensor([[0,1],[1,0],[0,1],[0,1]])
    input3=torch.Tensor([[1,1],[0,0],[0,0],[1,1]])
    input_list=[input1,input2,input3]
    for input_value in input_list:
        out=model(input_value)
        print(input_value,"\n",out)
        print("-"*50)
# %%
