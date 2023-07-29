---
layout: page
title: w2kplot  
description: A post-processing library for DFT calculations in Wien2k
img: assets/img/w2kplot.png
importance: 1
category: tools
related_publications: 
giscus_comments: true
---


**w2kplot** is a [Matplotlib](https://matplotlib.org) wrapper written in Python to create publication quality plots from data generated from the [WIEN2k](http://susi.theochem.tuwien.ac.at) density-functional theory (DFT) code.

### Examples


Here's example of plotting the orbital character on top of the bands a.k.a, a _fatband_ plot.
<div class="row">
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/fatband.png" title="fatband" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

We can easily create subplots with different band structure files.
<div class="row">
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/spinpol.png" title="spinpolarized" class="img-fluid rounded z-depth-1" %}
    </div>

</div>

The API is extremely intuitive and should feel familiar to the matplotlib API. Here's a quick example to create a band structure plot.

```python
	# plot basic band structure
	from w2kplot.bands import Bands, band_plot
	
	plt.figure()
	dft_bands = Bands(spaghetti='case.spaghetti_ene', klist_band='case.klist_band')
	band_plot(dft_bands, 'k-', lw=1.5)
	plt.show()
```

**w2kplot** has a command line interface (cli) for quickly viewing results and testing. A band structure can be plotted from the case directory by executing ``w2kplot-bands``. Similarily, the orbital character ("fatbands") can be generated from ``w2kplot-fatbands``. The entire list of options that allow you to drive these two tools are shown below.
