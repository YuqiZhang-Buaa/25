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

class DynamicKernelFusion(nn.Module):
    def __init__(self, d_dim, k_dim=16):
        super().__init__()
        self.k_gen = nn.Linear(3*d_dim, k_dim*d_dim)
        self.k_dim = k_dim
        
    def forward(self, x, y, z):
        B, L, D = x.shape
        kernel = self.k_gen(torch.cat([x,y,z], -1)).view(B, L, D, self.k_dim)
        return torch.einsum('bldk,bld->bld', kernel, x*y)