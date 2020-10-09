

def get_features(pair1, pair2):
    import numpy as np
    from scipy.spatial import distance
    featmat = []
    for i in range(0,pair1.shape[0]):
        tempfeat= []
        tempfeat.append(distance.euclidean(pair1[i,:],pair2[i,:]))
        tempfeat.append(distance.sqeuclidean(pair1[i,:],pair2[i,:]))
        tempfeat.append(distance.minkowski(pair1[i,:],pair2[i,:], p=1))
        tempfeat.append(distance.cosine(pair1[i,:],pair2[i,:]))
        tempfeat.append(distance.correlation(pair1[i,:],pair2[i,:]))
        tempfeat.append(distance.chebyshev(pair1[i,:],pair2[i,:]))
        featmat.append(tempfeat)
    featmat = np.asmatrix(featmat)
    featmat = np.nan_to_num(featmat)
    return featmat
