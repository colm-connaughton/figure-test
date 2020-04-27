import matplotlib.pyplot as plt

def standard_plot(dataframe, columns, labels, ratio=1.0):
    # Create figure and axes objects for plotting to
    fig=plt.figure()
    ax = plt.axes()

    # Add the specified columns from the dataframe to the plot
    for tag in columns:
        label =  labels[tag]
        dataframe[tag].plot(label=label, ax=ax)

    # Set some plot features
    ax.set_aspect(1./(ratio*ax.get_data_ratio()))
    plt.legend(loc='upper right', ncol=1, mode="expand", framealpha=1.0)

    # Return the figure and axis objects for subsequent tweaking
    return fig, ax
