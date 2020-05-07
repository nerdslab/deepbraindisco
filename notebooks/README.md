## Data

Our <a href = "http://bossdb.org/project/prasad2020" target = "_blank">dataset</a> consists of a 3D brain volume, generated via microCT, spanning from hypothalamus to cortex. It has the dimensions 720x1420x5805 (z,y,x), with a 1.17um isotropic voxel volume. The brain areas available are Cortex, Striatum, Ventral Posterior, Zona Incerta, Hypothalamus, and White Matter (Internal Capsule + Corpus Callosum).
The data was collected, processed and analyzed by Prasad et al. as described in the paper, "<a href="http://bossdb.org/project/prasad2020" target="_blank">A three-dimensional X-ray microtomography thalamocortical dataset for characterizing brain heterogeneity</a>".

![](/images/png_259.png)
<div align="center">Example of slice 0259 in the dataset</div>

#### Relevant data
- <a href="https://www.dropbox.com/s/n0tkvx1gsk57vky/img_slices.zip?dl=0" target="_blank">Images for slices 0159, 0209, 0259, and 0359</a>
- <a href="https://www.dropbox.com/s/ltrtoo4c02f7412/usual_order_annos_noTRN_0259.npy?dl=0" target="_blank">ROI annotations for slice 0259</a>

## Deep feature learning approach for neuroanatomical discovery

In order to be able to model neural microstructure directly from brain imagery, we first train a deep convolutional neural network (CNN) that can discriminate between different brain regions in the sample using only local views of ROIs. Restricting the network to only look at local information when identifying a particular brain region forces it to pay attention to and learn how to model specific anatomical features of the dataset, thus encouraging it to build rich feature sets such as the patterning of axons, morphology of cells, etc.

Once we have a well trained network that can successfully encode the relationships between the different ROIs in the sample, we pass many patches through the network and extract the activations for the same at the last hidden layer of the network. These activations can be thought of as efficient codes of the inputs that they correspond to, and typically comprise of task-specific features that are essential for the brain region discrimination task that the network was trained to do.

The extracted activations are then collected and arranged into a matrix on which we apply dimensionality reduction via matrix factorization, viz. principal component analysis (PCA) and non-negative matrix factorization (NMF). The resulting low-dimensional manifolds provide us with important information about how the network encodes certain aspects of the data and give us a lens into how the different ROIs are organized with respect to each other within the network. More importantly, these manifolds also give us a way of exploring the _latent factors_ of the data and learning how certain microstructural primitives are encoded in the network.

![](/images/overview_DeepBrainDisco.png)
<div align="center">Overview of the DeepBrainDisco pipeline</div>

### Relevant data and notebooks:
- <a href="https://www.dropbox.com/s/vtiyl8sq4wxpa64/Data_Subset2.zip?dl=0" target="_blank">Curated train, validation and test datasets used for training and model selection</a>
- <a href="https://www.dropbox.com/s/q51rgk69cz90jn0/cnn_weights.pt?dl=0" target="_blank">Weights of the trained model</a>
- <a href="https://github.com/nerdslab/deepbraindisco/blob/master/architecture.py" target="_blank">Model architecture</a>
- <a href="https://github.com/nerdslab/deepbraindisco/blob/master/notebooks/extract_activations_train_val_test.ipynb" target="_blank">Jupyter notebook to i) load model architecture and weights, ii) test the model on the train, validation and test datasets, and, iii) collect activations across the three datasets</a>

## Revealing localized macrostructure with NMF

Different matrix factorization techniques differ in the constraints that they impose on the factors to be produced, thus giving their subsequent embeddings different properties. We found that the non-negativity constrain imposed by NMF was sufficient to generate *sparse* and *localized* factorizations of the representations collected. In this case, the embeddings of images onto these factors reveals different groupings or clusters within and across brain regions.

![](/images/resized_rot_factors.png)
<div align="center">Sparse and localized NMF coefficients (embeddings) across a full slice</div>

#### Relevant data and notebooks:
- <a href="https://www.dropbox.com/sh/r3ucfrlyoe9yyie/AACvGrIBu4OFhXYZm_bqOXZUa?dl=0" target="_blank">Network representations extracted from densely sampled patches and their locations in slices 0259, 0359</a>
- <a href="https://github.com/nerdslab/deepbraindisco/blob/master/notebooks/combined_reps_NMF-0259.ipynb" target="_blank">Jupyter notebook to generate non-negative factors from network activations (slice 0259)</a>
- <a href="https://www.dropbox.com/sh/tsjwi82uzydogm2/AAA_3U8XiAe0hr5RxPgPj5wMa?dl=0" target="_blank">15D NNMF representations for slices 0259, 0359</a>
- <a href="https://github.com/nerdslab/deepbraindisco/blob/master/notebooks/Select_topK_NMF_factors.ipynb" target="_blank">Jupyter notebook to subselect localized predictive non-negative factors across slices 0259, 0359</a>

## Discovering new anatomical motifs and ROIs

Visualizing the different NMF embeddings makes it clear that the factors cause co-expression in areas with similarities in terms of their cell densities or local axonal projection patterns. We therefore chose to investigate the different factors' expressions in the cortex and found that fitting a gaussian mixture model on the non-negative factors allowed us to cluster roughly by cell density, thus allowing us to pull out both laminar differences and barrel fields, without any prior knowledge of these modtifs. These findings point to the fact that deep learning-based representations can be used to find finer sub-divisions and biological features in the data, even when they’re not trained explicitly to do so. We hope that  these results can be advanced and further translated into approaches for disease diagnosis, continuous variability modeling in brain structure, and to discover micro-architectural motifs in new areas.

![](/images/fig5_edits_combo_jpg.jpg)
<div align="center">Different factors clustered via GMM on the NMF embeddings, and their results overlaid on the original image (slice 0259)</div>

## Relevant data and notebooks:
- <a href="https://www.dropbox.com/sh/psr95swt7ipaxrp/AAAbB-14dEGFfm5HtSPuh3YZa?dl=0" target="_blank">Cortical layer annotations for slices 0259, 0359</a>
- <a href="https://www.dropbox.com/sh/pw0vadyuymemiye/AACGMiuXqogZLDlrRK937KVKa?dl=0" target="_blank">Cortical network activations for slices 0259, 0359</a>
- <a href="https://github.com/nerdslab/deepbraindisco/blob/master/notebooks/Select_topK_NMF_factors.ipynb" target="_blank">Jupyter notebook to subselect predictive cortical NMF factors in the cortex for slices 0259, 0359</a>
- <a href="https://github.com/nerdslab/deepbraindisco/blob/master/notebooks/Cortex_clustering_GMM_analyses_no_outliers_0259_0359.ipynb" target="_blank">Jupyter notebook to i) remove outlier samples in the cortex, ii) fit GMMs to the remaining samples' NMF factors, iii) match subsequent clusters, and, iv) Overlay GMMs on original images, all across slices 0259 and 0359</a>

## Team
- Aishwarya H. Balwani ([AishwaryaHB](https://github.com/AishwaryaHB))
- Eva L. Dyer ([evadyer](https://github.com/evadyer))

