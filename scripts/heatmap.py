#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time

a = np.random.random((16,16))
plt.imshow(a, cmap = 'hot', interpolation = 'nearest')
plt.show()
