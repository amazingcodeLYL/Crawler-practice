#plot画图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# data=pd.Series(np.random.randn(1000),index=np.arange(1000))
# data.cumsum()#累加数据
# data.plot()
# plt.show()

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
data.cumsum()
data.plot()
plt.show()