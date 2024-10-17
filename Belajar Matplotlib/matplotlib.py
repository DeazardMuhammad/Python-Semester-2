import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10, 15, 20, 25])
ypoints = np.array([0, 250, 100, 300])
# ypoints = np.array([10, 10, 20, 20,10])
# xpoints = np.array([0, 5, 5, 0,0])

# plt.plot(xpoints, ypoints)
# plt.plot(ypoints, marker = 's')
# plt.plot(ypoints, ls = 'dashed')
# plt.plot(ypoints, color = 'r')

# plt.plot(xpoints, ypoints)
# plt.show()


############### Subplot
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])


# plt.subplot(1,2,2)
# plt.plot(x,y, ls='dotted', color = 'g')
# plt.title("Hotel 1")
# plt.grid()

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])


# plt.subplot(1,2,2)
# plt.plot(x,y, ls='dashed', color = 'r')
# plt.title("Hotel 2")
# plt.grid()

# plt.show()


############ Scatter
# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([10, 15, 20, 25])
# ypoints = np.array([0, 5, 2, 8])
# plt.scatter(xpoints, ypoints)

# ypoints = np.array([ 10, 20, 20,10])
# xpoints = np.array([ 0, 5, 2,8])
# plt.scatter(xpoints, ypoints)

# plt.grid()
# plt.show()