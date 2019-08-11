Title: Traffic Metrics and 5 Source Code Search Sites
Date: 2008-12-24
Category: Articles
Tags: data science

Competitive research and traffic analysis is an important part of launching a new
site or web app.

![Alexa Toolbar](/images/alexa_toolbar.jpg "Alexa Toolbar")

I did a quick study that uses source code search sites as the subject for comparison.
Here I  highlight some key metrics from these two Firefox add-ons:

* [Google Toolbar](http://toolbar.google.com)
* [Alexa Toolbar & Sparky](http://www.alexa.com/site/download)

I found these sites through my delicious bookmarks, search, and the "Similar Pages"
and "Related Links" features of both of the above add-ons

<table class="table">
<tr>
    <th>Source Code Search Site</th>
    <th>Alexa Traffic Rank</th>
    <th>CoolGoogle PageRanke</th>
</tr>
<tr>
    <td>Google.com/codesearch</td>
    <td>2</td>
    <td>7</td>
</tr>
<tr>
    <td>Koders.com</td>
    <td>34642</td>
    <td>6</td>
</tr>
<tr>
    <td>Krugle.com</td>
    <td>113268</td>
    <td>5</td>
</tr>
<tr>
    <td>Codefetch.com</td>
    <td>175389</td>
    <td>4</td>
</tr>
<tr>
    <td>Codease.com</td>
    <td>179759</td>
    <td>4</td>
</tr>
</table>

First, you have to take these rankings with a grain of salt. Google's PageRank seems to honor the difference between google.com (10) and google.com/codesearch (7). Alexa's Traffic Rank (2) does not honor the difference and uses the ranking for Google's main domain instead.

Another useful metric is unique visitors seen here from compete.com:
<http://siteanalytics.compete.com/koders.com+krugle.com+codease.com/?metric=uv>

![Compete: Code Search Sites](/images/compete.png "Compete: Code Search Sites")

For a quick look at how the search results look for these sites,
I plugged in Spring's verbosely named
AbstractTransactionalDataSourceSpringContextTests. Here are some links to the results:

* http://www.google.com/codesearch?q=AbstractTransactionalDataSourceSpringContextTests&hl=en&btnG=Search+Code
* <http://www.koders.com/default.aspx?s=AbstractTransactionalDataSourceSpringContextTests&btn=&la=*&li=*>
* <http://www.krugle.org/kse/entfiles?query=AbstractTransactionalDataSourceSpringContextTests>
* <http://codase.com/search/text?join=abstracttransactionaldatasourcespringcontexttests+&scope=join%2Fjoin>

If you'd like to mention more sites like this, please share in the comments!
