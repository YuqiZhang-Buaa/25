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

class SimpleAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.query = nn.Linear(512, 512)
        self.key = nn.Linear(512, 512)
        
    def forward(self, features_list):
        queries = [self.query(f.mean(dim=1)) for f in features_list]  # [B, D]
        keys = [self.key(f) for f in features_list]  # [B, L, D]
        attns = [torch.softmax(q @ k.transpose(1,2), dim=-1) for q,k in zip(queries, keys)]
        return sum(a @ f for a,f in zip(attns, features_list)) / len(features_list)