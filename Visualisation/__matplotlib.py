import matplotlib.pyplot as plt
import numpy as np


def first_part():
    x = np.arange(10)
    y = 2 * x
    z = 3 * x
    a = 4 * x
    print(x)
    print(y)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.plot(x, a)
    plt.xlim(0,6)
    plt.ylim(0,24)
    plt.title("Simple graphic")
    plt.xlabel("Argument")
    plt.ylabel("Value")
    plt.savefig("test.png")
    plt.show()
def second_part():
    a = np.linspace(0,10,11)
    b = a ** 4
    print(a)
    print(b)
    x = np.arange(0,10)
    y = 2 * x
    print(x)
    print(y)
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
    axes.plot(a,b)
    axes.set_xlim(0,8)
    axes.set_ylim(0,8000)
    axes.set_xlabel("a")
    axes.set_ylabel("b")
    axes.set_title("Power 4")
    axes2 = fig.add_axes([0.2,0.5, 0.25, 0.25])
    axes2.plot(a,b)
    axes2.set_xlim(1,2)
    axes2.set_ylim(0,50)
    axes2.set_xlabel("a")
    axes2.set_ylabel("b")
    axes2.set_title("Power 4 increased")
    plt.show()
def third_part():
    fig = plt.figure(figsize=(1,8))
    axes1 = fig.add_axes([0, 0, 1, 1])
    a = np.arange(0, 10)
    b = a * 4
    axes1.plot(a,b)
    fig.savefig("test2.png")
def fourth_part():
    fig, axes = plt.subplots(nrows=3,ncols=2)
    a = np.linspace(0,10,11)
    b = a ** 4

    x = np.arange(10)
    y = 2 * x

    n = np.arange(4)
    m = np.sin(n)
    print(type(axes))
    print(axes.shape)
    axes[0][0].plot(a,b)
    axes[1][1].plot(x,y)
    axes[2][1].plot(n,m)
    axes[0][0].set_title("Simple title")
    axes[1][1].set_ylabel("Y Label")
    fig.suptitle("Figure general title")
    fig.subplots_adjust(wspace=0.9, hspace=0.8)
    ##plt.tight_layout()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.show()
def fifth_part():
    fig = plt.figure()
    axes = fig.add_axes([0.1,0.1,0.9,0.9])
    x = np.linspace(0, 11,10)
    axes.plot(x,x, label = "X vs X")
    axes.plot(x, x**2, label = "X vs X^2")
    axes.legend(loc = (0.8, 0.5))
    plt.show()

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,1,1])
x = np.arange(0,10)
ax.plot(x,x,color="orange", linewidth=5, linestyle="--")
ax.plot(x,2 * x, color="green", linewidth=1.5, linestyle="-.")
lines = ax.plot(x, 3 * x, color = "purple", linewidth=4)
lines[0].set_dashes([1,1,1,2,3,5])
ax.plot(x,x+1,linewidth=2,marker="s", linestyle="--", markersize=10, markeredgecolor="red", markeredgewidth=4, markerfacecolor="green")
ax.plot(x,x+3,linewidth=2,marker="+", linestyle="--")
plt.show()


