import numpy as np

null_outcomes = []

click_outcomes = ["click", "no click"]

rng = np.random.default_rng(200)

for i in range(10000):
    simulated_users = rng.choice(click_outcomes, size=500, p=[0.65, 0.35])

    num_clicked = np.sum(simulated_users == "click")

    null_outcomes.append(num_clicked)

print(np.percentile(null_outcomes, [2.5, 97.5]))
