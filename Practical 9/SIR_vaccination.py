# SIR Model with Vaccination
# This code simulates the spread of an infectious disease using the SIR model, incorporating different vaccination rates. The population is divided into three compartments: susceptible (S), infected (I), and recovered (R). The simulation runs for a specified number of time steps, updating the counts of each compartment based on the infection and recovery probabilities, as well as the initial number of vaccinated individuals. Finally, it plots the results to visualize the effect of vaccination on the disease spread over time.  
import numpy as np
import matplotlib.pyplot as plt
# initialization
N = 10000
beta = 0.3
gamma = 0.05

vacc_rates = np.linspace(0,1,11) # vaccination rates from 0% to 100%
# loop over vaccination rates
for v in vacc_rates:

    vaccinated = int(N * v)
    R = vaccinated
    I = 1 if (N-R) else 0
    S = max(0, N - R - I)
    I_list = [I]
# time loop
    for t in range(500):
        infection_prob = beta * (I / N)

        new_infections = np.random.binomial(S, infection_prob)
        new_recoveries = np.random.binomial(I, gamma)

        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        I_list.append(I)
# plot results
    plt.plot(I_list, label=f"Vacc={int(v*100)}%")

plt.xlabel("Time")
plt.ylabel("number of people")
plt.title("SIR model with different Vaccination")
plt.legend()
plt.show()