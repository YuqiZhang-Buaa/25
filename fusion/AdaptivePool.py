import numpy as np
import torch
import torch.nn as nn
import math
from math import ceil
from mamba_latest.mamba_ssm import Mamba2_change
from mamba_latest.mamba_ssm import Mamba2
import torch.nn.functional as F
from einops import rearrange, reduce
from torch import nn, einsum
import sys

class AdaptivePoolFusion(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.ones(3))
        
    def forward(self, features_list):
        norm_weights = F.softmax(self.weights, dim=0)
        pooled_features = [reduce(f, 'b l d -> b d', 'max') for f in features_list]
        # print('pooled_features[0].shape:', pooled_features[0].shape)
        return sum(w * f for w, f in zip(norm_weights, pooled_features))