# em-pokemon-go-std-dev
Expectation Maximization demonstration by using a Gaussian Mixture Model with available Pokemon GO data
Right now, we have a dataframe with the names of all OG 151 Pokemon as rows
and their respective weight, height, and equivalent standard deviations as
columns. To turn this into a GMM, we would need to convert each row into a
Gaussian based off of the mean and standard deviation for both the height and
weight of the Pokemon (2D Gaussian).

A 2D Gaussian would have a mean vector for its mean value and a covariance
matrix for its standard deviation value. We have a few issues here:

1. We don't know how to design the covariance matrix as the relation between
a Pokemon's height and its weight is unknown.

2. Real life Pokemon GO height and weight values are typically truncated,
so that they aren't above or below a certain value per species (this feature
has been historically very buggy in the game, with certain Pokemon being able
to directly circumvent these truncated values). If we want to implement this,
we'd need to truncate a multivariate Gaussian, which can be difficult in
prractice.

The first issue isn't a problem if we just assume no correlation between the
two values, as they aren't specified in the protobuf to be correlated. There
probably is significant covariance between the two, but we can judge that
at a later time.
The second issue isn't as much of a problem if we choose to ignore the traditional
truncations, which I'll opt to do for now.