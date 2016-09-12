from sklearn.datasets import *
import numpy as np
import matplotlib.pyplot as plt
from sequential import BSAS
from validity_scripts import internal_criteria, external_criteria, relative_criteria
from scipy.stats import norm
from tqdm import tqdm
from sys import maxsize as max_integer
from utility.plotting_functions import *

import unittest

plt.style.use('ggplot')

class Test(unittest.TestCase):


    @unittest.skip("no")
    def testBlobs(self):
        no_of_clusters = 4
        
        # Create the dataset
        X, y = make_blobs(n_samples = 500, centers= no_of_clusters, n_features=2,random_state=121)
        
        # Run the clustering algorithm
        X, centroids, no_of_clusters = BSAS.basic_sequential_scheme(X, threshold = 8)

        # Plotting
        plot_data(X, no_of_clusters, centroids)
        
        # Examine Cluster Validity with statistical tests
        initial_gamma, list_of_gammas, result = internal_criteria.internal_validity(X, no_of_clusters, BSAS.basic_sequential_scheme)
        initial_indices, list_of_indices, result_list = external_criteria.external_validity(X, no_of_clusters, y, BSAS.basic_sequential_scheme)
        
        # Histogram of gammas from internal criteria 
        hist_internal_criteria(initial_gamma, list_of_gammas, result)
        hist_external_criteria(initial_indices, list_of_indices, result_list)
        
        plt.show()
    
    @unittest.skip("no")
    def testCircles(self):
        # Create the dataset
        X, y = make_circles(n_samples=500, shuffle = True, noise = 0.05, factor = 0.5, random_state = 121)
        
        # Run the clustering Algorithm
        X, centroids, no_of_clusters = BSAS.basic_sequential_scheme(X, threshold = 1.1)
        
        # Plotting
        plot_data(X, no_of_clusters, centroids)
        
        # Examine Cluster Validity with statistical tests
        initial_gamma, list_of_gammas, result = internal_criteria.internal_validity(X, no_of_clusters , BSAS.basic_sequential_scheme)
        initial_indices, list_of_indices, result_list = external_criteria.external_validity(X, no_of_clusters, y, BSAS.basic_sequential_scheme)
        
        # Histogram of gammas from internal and external criteria 
        hist_internal_criteria(initial_gamma, list_of_gammas, result)
        hist_external_criteria(initial_indices, list_of_indices, result_list)
        
        plt.show()
        
    #@unittest.skip("no")
    def testMoons(self):
        # Create the dataset
        X, y = make_moons(n_samples=500, shuffle = True, noise = 0.1, random_state = 121)
        
        # Run the clustering algorithm
        X, centroids, no_of_clusters = BSAS.basic_sequential_scheme(X, threshold = 1)
        
        # Plotting
        plot_data(X, no_of_clusters, centroids)
        
        # Examine Cluster Validity with statistical tests
        initial_gamma, list_of_gammas, result = internal_criteria.internal_validity(X, no_of_clusters, BSAS.basic_sequential_scheme)
        initial_indices, list_of_indices, result_list = external_criteria.external_validity(X, no_of_clusters, y, BSAS.basic_sequential_scheme)
        
        # Histogram of gammas from internal and external criteria 
        hist_internal_criteria(initial_gamma, list_of_gammas, result)
        hist_external_criteria(initial_indices, list_of_indices, result_list)
        
        plt.show()

################################################## Relative Criteria Clustering #########################
    
    @unittest.skip('no')
    def testRelativeBlobs(self):
        no_of_clusters= 4
        
        # Create the dataset
        X, y = make_blobs(n_samples=500, centers= no_of_clusters, n_features=2,random_state=121)
        
        # Successive executions of the clustering algorithm
        no_of_clusters_list, DI, DB, SI= relative_criteria.relative_validity_hard_sequential(X)

        # Plot the indices
        plot_relative_criteria_sequential(no_of_clusters_list, DI, DB, SI)
        plt.show()         
    
    @unittest.skip('no')
    def testRelativeCircles(self):

        # Create the dataset
        X, y = make_circles(n_samples=500, shuffle = True, noise = 0.05, factor = 0.5, random_state = 121)
        
        # Successive executions of the clustering algorithm
        no_of_clusters_list, DI, DB, SI= relative_criteria.relative_validity_hard_sequential(X)

        # Plot the indices
        plot_relative_criteria_sequential(no_of_clusters_list, DI, DB, SI)
        plt.show()     
    
    
    @unittest.skip('no')
    def testRelativeMoons(self):

        # Create the dataset
        X, y = make_moons(n_samples=500, shuffle = True, noise = 0.07, random_state = 121)
        
        # Successive executions of the clustering algorithm
        no_of_clusters_list, DI, DB, SI = relative_criteria.relative_validity_hard_sequential(X)

        # Plot the indices
        plot_relative_criteria_sequential(no_of_clusters_list, DI, DB, SI)
        plt.show()  
                
                
                




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()