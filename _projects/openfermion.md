---
layout: page
title: Learn OpenFermion-FQE
description: Simulating the 1D Fermi-Hubbard model in OpenFermion-FQE.
importance : 1
category : learn
---

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/openfermion.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/openfermion.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
    {% jupyter_notebook jupyter_path %}
{% else %}
    <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}
