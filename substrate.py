from torch.utils.data import Dataset
import torch

class Information(Dataset):
    def __init__(self, input, output):
        self.source = torch.stack(input)
        self.transducer = torch.stack(output)
      
    def __getitem__(self, variable):
        return self.source[variable], self.transducer[variable]
      
    def __len__(self):
        return len(self.source)
