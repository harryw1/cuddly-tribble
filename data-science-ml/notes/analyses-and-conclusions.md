# Data Analyses and Conclusions

This module discusses five major kinds of data analyses. These analyses are:
1. Descriptive Analysis
2. Exploratory Analysis
3. Inferential Analysis
4. Causal Analysis
5. Predictive Analysis

## Descriptive Analysis

From Codeacademy:
> Descriptive analysis lets us describe, summarize, and visualize data so that patterns can emerge.Sometimes we'll only do a descriptive analysis, but often we'll use it as a first step in our process.

Descriptive analyses usually include measures of central tendency like mean, median, and mode, as well as measures of dispersion.

Data visualization is also typically included in descriptive analysis.

## Exploratory Analysis

Typically after descriptive analysis, we move on to exploratory analysis. This is where we start to look for patterns and relationships in the data, more specifically, relationships between variables.

Again, exploratory analysis cannot tell us why these relationships exist, but it can help us to identify them. "Correlation does not imply causation."

### Clustering

Another technique used in exploratory analysis is clustering. Clustering is a type of unsupervised machine learning that groups data points together based on their similarities.

## Inferential Analysis

Inferential analyses let us test hypotheses and understand relationships between variables. This is where we start to make inferences about the population based on the sample data.

An example of inferential analysis is A/B testing. I see this sort of thing all the time on YouTube, where they test different thumbnails to see which one gets more clicks.

> Imagine we want to know if a blue or a green button will get more clicks on a website. We hypothesize that the green button will be more successful and we run an A/B test on a sample of people that visit our site. Half the sample sees the blue button (option A) and half see the green button (option B). At the end of the test, 90% of people that saw the green button clicked it, whereas 60% of the people that saw the blue button clicked it. Now we need to ask, “If color wasn’t related to click rate, how likely was a 30% difference just by chance?” We can use statistics to calculate that probability. If there is less than a 5% probability that our results happened by chance, we have good evidence that green buttons get more clicks! We can extend these results to everyone that visits our site (the whole population), so it makes sense to use green buttons on our website.

Some rules of thumb:

- Sample size matters. The larger the sample size, the more confident we can be in our results. A sample size of 10% of the population is a good rule of thumb.
- Random sampling is important. We want our sample to be representative of the population.
- We can only test one hypothesis at a time.

## Causaul Analysis

Causal analysis is where we start to ask why things are happening. This is where we start to look at the mechanisms behind the relationships we've identified in our exploratory and inferential analyses.

Causal analysis requires us to have experiments wher we only change one variable at a time, carefully controlling for other variables, and are repeatable with the same results.

### Causal Analysis with Observational Data

Sometimes we can't run experiments to repeat results. In this case, we can use observational data to try to infer causality. When we do this, we need to be very careful about the conclusions we draw.

Causal inference with observational data requires:
- Advanced techniques to identify causal relationships
- Meeting very specific and strict assumptions
- Appropriate statistical methods and tests

## Predictive Analysis

Sometimes we interact with predictive analysis without even realizing it. For example, when we use Google Maps to find the fastest route to work, we're using predictive analysis. Predictive analysis uses data and supervised machine learning to make predictions about the future based on past data and the likelihood of future events.

Some supervised machine learning techniques used in predictive analysis include:
- Regression models
- Support vector machines
- and Deep learning convolutional neural networks
