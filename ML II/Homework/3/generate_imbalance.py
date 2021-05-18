def get_data(n1,n2):
    dist1 = scipy.stats.multivariate_normal(mean = np.zeros(2),
                                    cov = np.diag(np.ones(2)))
    dist2 = scipy.stats.multivariate_normal(mean = np.ones(2),
                                    cov = np.diag(np.ones(2)))
    X = np.concatenate([dist1.rvs(size=n1), dist2.rvs(size=n2)], axis=0)
    y = np.array([0]*n1 + [1]*n2)
    return(X,y)

