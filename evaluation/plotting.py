import matplotlib.pyplot as plt
import pylab
import numpy as np


def plot_topn(data_file, topn=10, metric="mean"):
    # Access data file
    with open("results.txt") as f:
        data = f.read()
    data = data.split("\n")
    data = [line.split() for line in data]
    data = [line for line in data if len(line) == 5 and line[0] != "Global"]
    
    # Get relevant entries
    if metric.lower()[0] != "s": # Sort by ascending mean
        data = sorted(data, key=lambda data:data[2])
    else: # Sort by ascending standard deviation
        data = sorted(data, key=lambda data:data[4])  
    data = data[:topn]+data[-topn:]
    tags = [line[0] for line in data] # Prompt ID
    indecies = list(range(len(tags)))
    means = [float(line[2]) for line in data]
    stdvs = [float(line[4]) for line in data]
    
    # Plot data
    fig = plt.errorbar(indecies, means, stdvs, fmt='ok', lw=1)
    plt.ylabel('Mean and Standard Deviation')
    # Label x axis with prompt ID's
    plt.xticks(indecies, tags) 
    plt.show()
    # Adjust graph length based on size topn so labels are always legible
    plt.figure(figsize=(1.2 * topn, 5))
    # Widen x axis to so first and last entries don't fall on axis lines
    pylab.xlim([-1,topn*2])

    
def plot_all(data_file, metric="mean"):
    # Access data file
    with open("results.txt") as f:
        data = f.read()
    data = data.split("\n")
    data = [line.split() for line in data]
    data = [line for line in data if len(line) == 5 and line[0] != "Global"]
    
    # Get relevant entries
    if metric.lower()[0] != "s": # Sort by ascending mean
        data = sorted(data, key=lambda data:data[2])
    else: # Sort by ascending standard deviation
        data = sorted(data, key=lambda data:data[4])  
    tags = [line[0] for line in data] # Prompt ID
    indecies = list(range(len(tags)))
    means = [float(line[2]) for line in data]
    stdvs = [float(line[4]) for line in data]
    
    # Plot data
    fig = plt.errorbar(indecies, means, stdvs, fmt='ok', lw=1)
    plt.xticks([], [])
    plt.show()
    plt.figure(figsize=(25, 10))
    pylab.xlim([-1,len(data)])
    

if __name__ == "__main__":
    plt.clf()
    plot_all("results.txt")
    plt.clf()
    plot_topn("results.txt", topn=10)
