import statistics as stats

"""
stats.mean(data)
returns arithmetic mean of data

stats.harmonic_mean(data)
returns harmonic mean of data

stats.median(data)
returns median of data
for odd number of data returns middle element
for even number of data returns average of the 2 middle elements

stats.media_low(data)
returns lower median of data
for odd number of data returns middle element
for even number of data returns lower median element

stats.median_high(data)
returns higher median of data
for odd number of data returns middle element
for even number of data returns higher median element
"""

a = [1,3,5,7]
stats.median(a) # => 4
stats.median_low(a) # => 3
stats.median_high(a) # => 5

"""
stats.mode(data)
returns highest occuring value in data

stats.variance()
returns variance of data

stats.stdev()
returns standard deviation of data

stats.pvariance()
returns population variance of data

stats.pstdev()
returns population standard deviation of data
"""
