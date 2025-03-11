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

class HybridFusion(nn.Module):
    def __init__(self, dim, kernel_size, stride, act=nn.LeakyReLU, out_dim=None):
        super(MobiVari1, self).__init__()
        self.dim = dim
        self.kernel_size = kernel_size
        self.out_dim = out_dim or dim

        self.dw_conv = nn.Conv1d(dim, dim, kernel_size, stride, kernel_size // 2, groups=dim)
        self.pw_conv = nn.Conv1d(dim, self.out_dim, 1, 1, 0)
        self.act = act()

    def forward(self, x):
        # x = x.transpose(1, 2)
        out = self.act(self.pw_conv(self.act(self.dw_conv(x)) + x))
        return out + x if self.dim == self.out_dim else out