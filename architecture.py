import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

train_on_gpu = torch.cuda.is_available()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        
        ## conv layers
        self.conv1 = nn.Conv2d(3, 16, 7, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 5, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=0)
        self.conv4 = nn.Conv2d(64, 128, 3, padding=0)
        
        ## pooling layer
        self.pool = nn.MaxPool2d(2,2)
        
        ## fc layers
        self.fc1 = nn.Linear(128*6*6,1024)
        self.fc2 = nn.Linear(1024,64)
        self.fc3 = nn.Linear(64,6)
        
        ## dropout
        self.dropout = nn.Dropout(0.3)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))
        
        ## flatten before introducing fcs
        x = x.view(-1,6*6*128)
        
        x = self.dropout(x)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        latents = x
        x = self.dropout(x)
        x = self.fc3(x)
        return x, latents
    
## create the CNN
model = Net()

## load weights into model skeleton
model.load_state_dict(torch.load('cnn_weights.pt'))

