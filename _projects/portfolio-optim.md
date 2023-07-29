---
layout: page
title: Portfolio-Optim.jl   
description: Financial portfolio optimization in Julia
img: assets/img/portfolio-optim.png
importance: 4
category: fun
---


Here, we can generate our portfolio and optimize the allocations using the two supported optimizers: EfficientFrontier and MonteCarloOptimizer.

```julia
using PortfolioOptim

tickers = ["GOOG", "DIS", "FB", "AMZN", "AAPL", "TSLA"]
portfolio = build_portfolio(tickers, "2020-01-01", "2022-01-01")
target_returns = collect(0.1:0.01:0.8)
EF_results = EfficientFrontier(portfolio, target_returns)
MC_results = MonteCarloOptimizer(portfolio)
```

Here, we visualize the results from our portfolio optimization,

<div class="row">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/portfolio-optim.png" title="EffFrontier" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

