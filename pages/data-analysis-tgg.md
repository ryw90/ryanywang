title: data-analysis-tgg
title_long: Things I Learned About Data Analysis at TGG
edited: 2014-04-20
published: 2014-04-20
tags: data, thoughts
summary: I was lucky to work with very talented people at The Greatest Good. Here are some of the things I learned about data analysis there.

## Things I Learned About Data Analysis at TGG ##
written on 2014-04-20

1. *Keep it simple*. It is the analyst's job to separate core issues from
nonessential details. Whether it's a model or an analysis, simple things are
easier to reason about.

2. *Simple does not imply naive*. It's not necessary to constrain onself to simple
averages and sums in order to be understood. When many factors may influence an
outcome, you can reason about effects when all else is equal e.g. by choosing
sensible comparison groups. Here is a good [example](http://www.bloomberg.com/dataview/2014-04-17/how-americans-die.html).

3. *Data analysis should be actionable*. The compilation of raw facts and
figures should lead to recommendations on how to resolve a problem of interest.
Another way to say this is that analyses should seek to inform decision-making.

4. *Understand the data-generating process*. The credo  "correlation does not
imply causation" is a bit obnoxious, but there's a good point there. The analyst
should be aware of the factors, both measured and unmeasured, that affect a
relationship observed in the data.

5. *Be wary of random noise*. It is easy to misinterpret the results of natural
variation. I've often seen this come up in the context of measuring skill.
For example, you often observes that today's high performers do worse tomorrow
while today's low performers improve. In short timeframes, this typically has
little to do with effort or ability, and a lot to do with [regression to the mean](http://www.dangreller.com/temporary-highs-and-lows-regression-to-the-mean).


6. *Understand the data-collection process*. This is a corollary to the above.
Especially in business settings when you are asked to glean insight from "data
exhaust", the data at your disposal are often biased in some way. Selection
bias in the sample is almost always a problem.

7. *Look for natural experiments*. These are situations where two groups are
essentially the same except for an arbitrary difference in a variable of
interest, allowing you to draw causal conclusions from observational data. The
rub is that you have to make assume that you really do have random assignment.
See here for an interesting [example](http://freakonomics.com/2011/06/01/the-supreme-court-provides-a-dissertation-topic-for-a-budding-economist/).

8. *Data analysis is time-consuming*. And it frequently takes longer than you
would have expected.

9. *Test predictive models out of sample*. Estimating performance on a held-out
portion of the data is more reliable than simply looking at measures of model
fit. In particular, test the model but don't overfit.

10. *Be wary of ex-post information*. It's easy to accidentally include
information from the future when building a predictive model. Sometimes you will
realize this mistake when you try to make predictions in real-time and fail,
but other times you may simply poor performance and not understand why. For
example, if you want to work with [nonfarm payrolls](https://research.stlouisfed.org/fred2/series/PAYEMS)
, you should be aware that statistics are revised up to 2 months later.

11. *Data must be cleaned*. Raw data often (always?) contain errors. There
can be misspellings or incorrect entries. Machine-written data can suffer
from outages. Data from different systems are rarely consistent with each other.
Finally, even error-free data must be aggregated or reshaped into a format that
is suitable for the analysis of interest.

12. *Have expectations of the data*. A good way to ensure data accuracy, or at
least to catch errors, is to have expectations regarding summary statistics. For
example, if you are working with sales data, is the total sum sensible? Is it
still sensible when you group by weeks or months?

13. *Test hypotheses through experimentation*. It is hard to distinguish good
analysis from bad analysis. Doing so requires careful reasoning and typically
some level of domain knowledge. A simple but powerful way around this is to
use randomized experiments to evaluate consequential hypotheses.

14. *Data should not substitute for judgment*. Data typically leads to more
objectivity than other decision aids. However, the data rarely, if ever,
[speak for themselves](http://blog.revolutionanalytics.com/2013/03/let-the-data-speak-for-themselves.html)
Ultimately human judgment plays a large role in all parts of the process,
especially in interpreting results.
