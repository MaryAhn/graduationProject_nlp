import random

import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self, input_size,output_size):
        super(LinearRegression, self).__init__()

        self.input_size = input_size
        self.output_size = output_size
        self.linear = nn.Linear(input_size, output_size)

    def forward(self,x):
        y = self.linear(x)

        return y

def ground_truth(x):
    return 3 * x[:, 0] + x[:, 1] - 2 * x[:, 2]

def train(model, x, y, optim):
    optim.zero_grad()

    y_hat = model(x)
    loss = ((y-y_hat)**2).sum() / x.size(0)

    loss.backward()

    optim.step()

    return loss.data


batch_size = 1
n_epochs = 1000
n_iter = 1000

model = LinearRegression(3, 1)
optim = torch.optim.SGD(model.parameters(), lr=1e-4, momentum=0.1)

for epoch in range(n_epochs):
    avg_loss = 0

    for i in range(n_iter):
        x = torch.rand(batch_size, 3)
        y = ground_truth(x.data)

    loss = train(model, x, y, optim)

    avg_loss += loss
    avg_loss = avg_loss / n_iter

    x_valid = torch.FloatTensor([[.3,.2,.1]])
    y_valid = ground_truth(x_valid.data)

    model.eval()
    y_hat = model(x_valid)
    model.train()

    print(avg_loss, y_valid.data[0], y_hat.data[0,0])

    if(avg_loss<.00001):
        break