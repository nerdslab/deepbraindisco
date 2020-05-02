## Welcome to Deep Brain Discovery (DeepBrainDisco)!

Models of neural architecture and organization are critical for the study of disease, aging, and development. Unfortunately, automating the process of building maps of microarchitectural differences both within and across brains still remains a significant challenge.

In our previous work, "<a href="https://ieeexplore.ieee.org/document/9048805" target="_blank">Modeling Variability in Brain Architecture with Deep Feature Learning</a>", we showed that it is possible to leverage deep learning to build robust and expressive data-driven models of brain structure across multiple, heterogeneous brain regions. With Deep Brain Discovery, we build on and continue this line of work - we show how one can use the representations from these models to learn meaningful features for modeling neural architecture, and also give examples of how to utilize these new features to discover new regions of interest within a sample that share similar characteristics in terms of their anatomical composition. We make use of low-rank matrix factorization to project high dimensional features extracted from neural networks into a more tractable and interpretable lower-dimensional space, and build models with the new low-dimensional representations that can be used to find morphogically relevant patterns in the anatomy, directly from images.

We apply our methods to a thalamocortical slice of the mouse brain, and successfully resolve biologically meaningful subdivisions within brain regions, such as laminar layers and barrels in somatosensory cortex. 

## Data

Our dataset consists of a 3D brain volume, generated via microCT, spanning from hypothalamus to cortex. It has the dimensions 720x1420x5805 (z,y,x), with a 1.17um isotropic voxel volume. The brain areas available are Cortex, Striatum, Ventral Posterior, Zona Incerta, Hypothalamus, and White Matter (Internal Capsule + Corpus Callosum).
The data was collected, processed and analyzed by Prasad et al. as described in the paper, "A three-dimensional X-ray microtomography thalamocortical dataset for characterizing brain heterogeneity" and is publicly <a href = "http://bossdb.org/project/prasad2020" target = "_blank">available</a>.

<figure>
  <img src="/images/XZ_Reslice_VS0172_fullstack_cc_rot_crop0259.tif">
  <figcaption style="text-align:center">Example of slice 0259 in the dataset</figcaption>
</figure>

## Team
- Aishwarya H. Balwani ([AishwaryaHB](https://github.com/AishwaryaHB))
- Eva L. Dyer ([evadyer](https://github.com/evadyer))
