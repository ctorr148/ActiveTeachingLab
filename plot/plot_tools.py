import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import Axes3D


def currents(network):

    data = network.currents

    fig, ax = plt.subplots()
    ax.imshow(data)
    ax.set_aspect("auto")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
             rotation_mode="anchor")

    ax.set_title("Network currents history")
    ax.set_xlabel("Neuron")
    ax.set_ylabel("Iteration")

    plt.tight_layout()
    plt.show()


def present_weights(network):

    fig, ax = plt.subplots()
    # im = ax.contourf(network.weights)
    im = plt.imshow(network.weights)
    ax.set_aspect("auto")

    ax.set_title("Weights matrix")
    ax.set_xlabel("Neuron $i$")
    ax.set_ylabel("Neuron $j$")

    plt.tight_layout()

    fig.colorbar(im, ax=ax)
    plt.show()


def array_history_index(array_history, index, contour=False):
    assert index < len(array_history)

    fig, ax = plt.subplots()
    if contour:
        im = ax.contourf(array_history[index])
    im = ax.imshow(array_history[index])
    ax.set_aspect("auto")

    ax.set_title(f"Weights (iter={index})")
    ax.set_xlabel("Neuron $i$")
    ax.set_ylabel("Neuron $j$")

    plt.tight_layout()

    fig.colorbar(im, ax=ax)
    plt.show()


def array_element_change(array_history, alpha=0.7):
    assert len(array_history) > 0

    history = np.array(array_history)
    diff = np.diff(history, axis=0)

    fig, ax = plt.subplots()

    counter = 0
    for j in range(diff.shape[1]):
        for k in range(diff.shape[2]):
            a = np.zeros(diff.shape[0])
            for i in range(diff.shape[0]):
                a[i] = diff[i, j, k]
            ax.plot(a, alpha=alpha)
            counter += 1

    ax.set_title("Matrix element change")
    ax.set_xlabel("Iteration")
    ax.set_xticks(np.arange(diff.shape[0]))
    ax.set_ylabel("Point value change")

    plt.show()


def theoretical_weights(network, index):
    assert index < len(network.theoretical_weights_history)

    fig, ax = plt.subplots()
    # im = ax.contourf(network.theoretical_weights_history[index])  # fancy
    im = ax.imshow(network.theoretical_weights_history[index])
    ax.set_aspect("auto")

    ax.set_title(f"Theoretical weights (iter={index})")
    ax.set_xlabel("Neuron $i$")
    ax.set_ylabel("Neuron $j$")

    plt.tight_layout()

    fig.colorbar(im, ax=ax)
    plt.show()


def mean_weights(network):

    fig, ax = plt.subplots()
    ax.plot(network.weights_mean)

    ax.set_title("Weights learning rule")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Difference of means")

    plt.show()


def pattern_similarity(network):

    fig, ax = plt.subplots()
    ax.plot(network.pattern_similarity_history)

    ax.set_title("Pattern similarity")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Pattern match$^2$")
    ax.set_ylim((-0.1, 1.1))

    plt.show()


def energy(network):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.arange(0, network.num_neurons, 1)
    y = x
    x, y = np.meshgrid(x, y)
    z = np.copy(network.weights)

    for i in range(network.num_neurons):
        for j in range(network.num_neurons):
            z[i, j] *= network.currents[-1, j]

    ax.plot_surface(x, y, z, alpha=0.9, cmap="viridis", antialiased=True)

    ax.set_title("Energy landscape")
    ax.set_xlabel("Neuron $_i$")
    ax.set_ylabel("Neuron $_j$")
    ax.set_zlabel("Energy")

    plt.show()


def noise(network):

    fig, ax = plt.subplots()

    neurons_noise = network.noise

    for n_neuron in neurons_noise:
        ax.plot(n_neuron, linewidth=0.5, alpha=0.9)

    ax.set_xlabel("Iterations")
    ax.set_ylabel("Noise")

    plt.show()

