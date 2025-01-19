from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.pie(payment_method_freqs)
plt.axis('equal')
plt.show()

# or making a pie chart with labels and a legend
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

# string formatting to add percentages to the pie chart too
plt.pie(payment_method_freqs, autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)

plt.show()
