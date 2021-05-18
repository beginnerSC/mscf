def plot_digit(x):
    """Plot a single digit.

    `x` should be a numpy array of 256 values between 0 and 1, such as one row
    from threes.csv.

    You will still have to call plt.show() yourself, since this function doesn't
    do it (in case you want to make multiple plots in a grid or something). Feel
    free to change the colormap if you want.
    """

    plt.imshow(x.values.reshape((16,16)))
