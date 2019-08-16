Title: Data Science Blogging with Pelican
Date: 2019-08-06
Category: Articles
Tags: pelican, data science

![Data Science]({static}/images/data-science-1.png "Data Science")

I've been blogging on [Wordpress](https://wordpress.org) since 2007, but very infrequently, maybe somewhat due to the
workflow and platform. For many years now, most of the interesting content I create is in
[Jupyter](https://jupyter.org/) notebooks (certainly the more relevant content to my work these days). I wanted a way
to integrate this content into my blog, but realized that not all of the legacy content has aged well and a notebook
workflow using the current setup would likely be cumbersome.

I've used [nbviewer](https://nbviewer.jupyter.org/) to make web accessible versions of notebooks in the past, for
example:

* [Intro to Python for Financial Market Data](https://nbviewer.jupyter.org/github/degiere/python-finance-notebooks/blob/master/python-financial-market-data-visualization.ipynb)

Also with two notebooks from the recent [Data Visualization](https://www.coursera.org/learn/datavisualization)
course I completed, which is part of the [Data Mining Specialty](https://www.coursera.org/specializations/data-mining)
that I've been working towards. He/re are those in their original form to compare:

* [Visualizing Bitcoin Trust Networks](https://nbviewer.jupyter.org/github/degiere/python-finance-notebooks/blob/master/visualizing-bitcoin-otc-trust-network.ipynb)
* [Visualizing Historical Bitcoin Prices](https://nbviewer.jupyter.org/github/degiere/python-finance-notebooks/blob/master/visualizing-historical-bitcoin-prices.ipynb)

I've worked on a number of custom CMS projects before, including Drupal extensions, and once even a simple music content
manager for the fabulous [XLR8R Magazine](https://www.xlr8r.com/). I've never been that happy working in PHP though.
Extending Wordpress would mean going deep with PHP again.

Are there any options available in the ecosystem of my day to day Jupyter, markdown, python, and git workflow?

Inspired by the great results from the likes of [Jake VanderPlas](https://jakevdp.github.io/) and
[Chris Albon](https://chrisalbon.com/), and mostly using Peter Kazarinoff's super helpful
[How I Built This Site](https://pythonforundergradengineers.com/how-i-built-this-site-1.html),
I decided to give the python based static site generator [Pelican](http://getpelican.com) a try to publish Jupyter
Notebooks directly to [Github Pages](https://pages.github.com/). 

Long story short, I've enjoyed the process and end result so much that I've ported some old content and notebooks over
to the site you're reading right here! I'll keep incorporating relevant old content, and will likely be inspired to
publish more on this platform. Perhaps I'll even do some theme and plugin work! At least I'd like to get Pandas
Dataframe's rendering like they do natively, but we'll save that for another post...

## Resources

* <https://github.com/degiere/blog>
* <https://pages.github.com/>
* <https://getpelican.com/>
* <https://github.com/danielfrg/pelican-ipynb>
