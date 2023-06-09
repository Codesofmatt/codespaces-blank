import matplotlib.pyplot as plt
import pandas as pd
plotdata = pd.DataFrame({
    "2018":[57,67,77,83],
    "2019":[68,73,80,79],
    "2020":[73,78,80,85]},
    index=["Django", "Gafur", "Tommy", "Ronnie"])
plotdata.plot(kind='bar', stacked=True,figsize=(15, 8))

plt.title("FIFA ratings")

plt.xlabel("Footballer")

plt.ylabel("Ratings")
plt.show()