from setuptools import setup, find_packages

setup(name='secimtools',
    version='1.0.0',
    description='Metabolomics tools from the SECIM project',
    url='https://github.com/secimTools/SECIMTools',
    author='SECIM Project',
    author_email='apps@rc.ufl.edu',
    license='MIT',
    keywords="metabolomics secim anova pca random-forest",
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
    'lxml==3.3.3',
    'matplotlib==1.5.1',
    'matplotlib-venn==0.11.1',
    'mpld3==0.2',
    'numpy==1.11.0',
    'palettable==2.1.1',
    'pandas==0.18.1',
    'patsy==0.4.0',
    'pymc==2.3.6',
    'rpy2==2.3.10',
    'scikit-learn==0.18',
    'scipy==0.15.1',
    'seaborn==0.7.0',
    'statsmodels==0.6.1',
    'sympy==0.7.4.1'
    ],
    classifiers = [
    'Environment :: Console',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    scripts=[
    'scripts/anova_fixed.py',
    'scripts/bland_altmant_plot.py',
    'scripts/blank_feature_filtering_flags.py',
    'scripts/coefificient_variation_flags.py',
    'scripts/compound_identification.py',
    'scripts/data_rescalling.py',
    'scripts/distribution_features.py',
    'scripts/distribution_samples.py',
    'scripts/drop_flags.py',
    'scripts/hierarchical_clustering_heatmap.py',
    'scripts/imputation.py',
    'scripts/lasso_enet.R',
    'scripts/lasso_enet_var_select.py',
    'scripts/linear_discriminant_analysis.py',
    'scripts/log_transformation.py',
    'scripts/magnitud_difference_flags.py',
    'scripts/mahalanobis_distance.py',
    'scripts/merge_flags.py',
    'scripts/modulated_modularity_clustering.py',
    'scripts/multiple_testing_adjustment.py',
    'scripts/mzrt_match.py',
    'scripts/partial_least_squares.py',
    'scripts/principal_component_analysis.py',
    'scripts/random_forest.py',
    'scripts/retention_time_flags.py',
    'scripts/run_order_regression.py',
    'scripts/scatter_plot_2D.py',
    'scripts/scatter_plot_3D.py',
    'scripts/standardized_eucildean_distance.py',
    'scripts/subset_data.py',
    'scripts/summarize_flags.py',
    'scripts/svm_classifier.py',
    'scripts/threshold_based_flags.py'
    ]
)