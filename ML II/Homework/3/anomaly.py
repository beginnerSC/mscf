def get_data(n):
    #prior probabilities
    pi0 = (.5,.3,.2)
    n_each = [int(n*pi) for pi in pi0]
    #means
    mus = ((0,0),(2,4),(-4,2))
    Sigmas = [
        np.matrix(((1,-0.7),(-0.7,0.9)))*1.6,
        np.matrix(((1,0.8),(0.8,0.9)))*1.6,
        np.matrix(((1,0.8),(0.8,0.9)))*1.6
    ]
    
    gaussians = [scipy.stats.multivariate_normal(mean = mus[i],cov = Sigmas[i]) for i in range(3)]
    X = np.concatenate([gaussian.rvs(n_each[i]) for i, gaussian in enumerate(gaussians)], axis=0)    
    return(X)


