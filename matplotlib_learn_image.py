import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978,0.365348418405,0.423733120134,0.365348418405,0.439599930621,0.525083754405,
                0.423733120134,0.525083754405,0.651536351379]).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower') #origin还有upper 即colorbar反向对应
plt.colorbar(shrink=0.9)  #shrink 高度压缩

plt.xticks(())
plt.yticks(())
plt.show()