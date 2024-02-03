from torch.utils.data import Dataset
import torch

class Datum(Dataset):
    def __init__(self, input, output=None):
        # Stacking expecration tensor into one tensor state with definite value
        # e.g. [[states]] -> [[state]] : [[value]] -> [[state]] : [[some possible logical state], [some other possible logical state]]
        self.data = torch.stack(input)
        self.label = torch.stack(y)
      
    def __getitem__(self, idx):
        return self.data[idx], self.label[idx]
      
    def __len__(self):
        return len(self.data)
