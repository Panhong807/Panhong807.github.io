#  SIR Model Simulation
# This code simulates the spread of an infectious disease using the SIR (Susceptible-Infected-Recovered) model. The model divides the population into three compartments: susceptible (S), infected (I), and recovered (R). The simulation runs for a specified number of time steps, updating the counts of each compartment based on the infection and recovery probabilities. Finally, it plots the results to visualize the dynamics of the disease spread over time.
import numpy as np
import matplotlib.pyplot as plt

# initialization
N = 10000       
beta = 0.3   
gamma = 0.05

S = N - 1          
I = 1              
R = 0              
S_list = [S]
I_list = [I]
R_list = [R]

# time loop
for t in range(1000):

    infection_prob = beta * (I / N)
    new_infections = np.random.binomial(S, infection_prob)
    new_recoveries = np.random.binomial(I, gamma)

    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# plot results
plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")

plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("SIR model")
plt.legend()
plt.show()