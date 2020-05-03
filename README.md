## Welcome to Deep Brain Discovery a.k.a. DeepBrainDisco!

Models of neural architecture and organization are critical for the study of disease, aging, and development. Unfortunately, due to issues such as physical artifacts, process variations, and general variability in the different types and regions of samples, automating the process of building maps of microarchitectural differences both within and across brains still remains a significant challenge.

With the advent of deep learning however, the neuroscientific community now has a tool that can potentially be applied to large, heterogeneous image datasets for the purposes of effectively modeling neural architecture. In our work, "<a href="https://ieeexplore.ieee.org/document/9048805" target="_blank">Modeling Variability in Brain Architecture with Deep Feature Learning</a>", we showed that it is indeed possible to leverage deep neural networks to build robust and expressive data-driven models of brain structure across multiple, diversified brain regions. <a href="" target="_blank">Deep Brain Discovery</a> builds and continues this line of work - it shows how one can use representations from trained deep learning models to learn *meaningful features* for modeling neural architecture, and through vignettes presents ways to utilize these features for the discovery of new regions of interest within the sample that share similar characteristics in terms of their anatomical composition. 

## Data

Our <a href = "http://bossdb.org/project/prasad2020" target = "_blank">dataset</a> consists of a 3D brain volume, generated via microCT, spanning from hypothalamus to cortex. It has the dimensions 720x1420x5805 (z,y,x), with a 1.17um isotropic voxel volume. The brain areas available are Cortex, Striatum, Ventral Posterior, Zona Incerta, Hypothalamus, and White Matter (Internal Capsule + Corpus Callosum).
The data was collected, processed and analyzed by Prasad et al. as described in the paper, "<a href="http://bossdb.org/project/prasad2020" target="_blank">A three-dimensional X-ray microtomography thalamocortical dataset for characterizing brain heterogeneity</a>".

![](/images/png_259.png)
<div align="center">Example of slice 0259 in the dataset</div>

## Deep Feature Learning Approach for Neuroanatomical Discovery

In order to be able to model neural microstructure directly from brain imagery, we first train a deep convolutional neural network (CNN) that can discriminate between different brain regions in the sample using only local views of ROIs. Restricting the network to only look at local information when identifying a particular brain region forces it to pay attention to and learn how to model specific anatomical features of the dataset, thus encouraging it to build rich feature sets such as the patterning of axons, morphology of cells, etc.

Once we have a well trained network that can successfully encode the relationships between the different  in the sample, we pass many patches through the network and extract the activations for the same at the last hidden layer of the network. These activations can be thought of as efficient codes of the inputs that they correspond to, and typically comprise of task-specific features that are essential for the brai region discrimination task that the network was trained to do.

The extracted activations are then collected and arranged into a matrix on which we apply dimensionality reduction via matrix factorization, viz. Non-negative Matrix Factorization (NMF). 
![](/images/overview_trans1.png)

## Team
- Aishwarya H. Balwani ([AishwaryaHB](https://github.com/AishwaryaHB))
- Eva L. Dyer ([evadyer](https://github.com/evadyer))
