## Welcome to Deep Brain Discovery a.k.a. DeepBrainDisco!

Models of neural architecture and organization are critical for the study of disease, aging, and development. Unfortunately, due to issues such as physical artifacts, process variations, and general variability in the different types and regions of samples, automating the process of building maps of microarchitectural differences both within and across brains still remains a significant challenge.

With the advent of deep learning however, the neuroscience community now has a tool that can potentially be applied to large, heterogeneous image datasets for the purposes of effectively modeling neural architecture. In our work, "<a href="https://ieeexplore.ieee.org/document/9048805" target="_blank">Modeling Variability in Brain Architecture with Deep Feature Learning</a>", we showed that it is indeed possible to leverage deep neural networks to build robust and expressive data-driven models of brain structure across multiple, diversified brain regions. <a href="" target="_blank">Deep Brain Discovery</a> builds and continues this line of work - it shows how one can use representations from trained deep learning models to learn *meaningful features* for modeling neural architecture, and through vignettes presents ways to utilize these features for the discovery of new regions of interest within the sample that share similar characteristics in terms of their anatomical composition. 

## Data

Our <a href = "http://bossdb.org/project/prasad2020" target = "_blank">dataset</a> consists of a 3D brain volume, generated via microCT, spanning from hypothalamus to cortex. It has the dimensions 720x1420x5805 (z,y,x), with a 1.17um isotropic voxel volume. The brain areas available are Cortex, Striatum, Ventral Posterior, Zona Incerta, Hypothalamus, and White Matter (Internal Capsule + Corpus Callosum).
The data was collected, processed and analyzed by Prasad et al. as described in the paper, "A three-dimensional X-ray microtomography thalamocortical dataset for characterizing brain heterogeneity" and is publicly available.

![](/images/png_259.png)
<div align="center">Example of slice 0259 in the dataset</div>

## Team
- Aishwarya H. Balwani ([AishwaryaHB](https://github.com/AishwaryaHB))
- Eva L. Dyer ([evadyer](https://github.com/evadyer))
