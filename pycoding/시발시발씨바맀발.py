import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')
data_3rd = data[(data['Pclass'] == 3) & 
                (data["Age"] > 15)]
data_comp = data_3rd[["Age", "Fare", "Survived"]]


data_3rd.plot.scatter(x="Age", y="Fare", c='Survived',
                #   s="Pclass",
                  cmap=plt.cm.get_cmap('vanimo'))
plt.show()