import itertools

def quantile_grid(x, y, q):
    """Find points closest to the quantiles of x and y.

    This function takes points with coordinates (x, y) and a list of quantiles
    `q` in the interval [0, 1]. It returns a grid of indices in the data
    corresponding to points closes to the q(i) and q(j)th quantiles of x and y.
    Each row corresponds to a quantile of y, each column to a quantile of x.

    You will plot the points at these indices to see how the digits vary across
    your axes.

    """

    q = np.array(q)
    xq = np.percentile(x, 100 * q)
    yq = np.percentile(y, 100 * q)
    idx_list = np.zeros(len(q)**2, dtype=np.int_)
    i = 0

    for ypt, xpt in itertools.product(yq,xq):
        idx_list[i] = np.argmin((x - xpt)**2 + (y - ypt)**2)
        i += 1

    return idx_list.reshape((len(q), len(q)))
