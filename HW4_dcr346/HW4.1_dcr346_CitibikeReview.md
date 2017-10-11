# Citibike HW3_Assinment1 Citibike Review
### reviewing [pak348 Ipython notebook](https://raw.githubusercontent.com/danachermesh/PUI2017_pak348/master/HW3_pak348/Homework_3_Assignment_2_pak348.ipynb)

### (a) Null and alternative hypotheses
The Null hypothesis was formulated correctly, though the **\alpha was not stated**.

The Alternative hypothesis was formulated correctly, though the **\alpha was not stated**. Moreover, instead of writing "Subscribers take **_more_** rides on Citibikes than Customers during Weekdays" it would be better to write **"..._significally_ more..."**

### (b) Verify that the data supports the project

* I am referreing for the UserType/Tripduration and not reviewing the efforts to analyze age of bikers. 

Please see cells of code + the following figures:
1. Figure 1a: ___Distribution of Citibike bikers by Customer types in July 2017, absolute counts___ 

2. Figure 1b: ___Distribution of Citibike bikers by Customer types in July 2017, absolute counts, with statistical errors___ 

3. Figure 1c: ___Distribution of Citibike bikers by Customer types in July 2017, Normalized___

The data supports the project.

However, considering the question is reffering for weekdays only, Saturday and Sunday information could have been neglected.

I would have suggest, instead of overseeing weekend data, to try and assess the differences between weekdays and weekends.

### (c) Chose an appropriate test to test H0 given the type of data
I chose t test to compare the costumers distribution with the users distribution. The reason is the fact that this is an analysis of two samples of a dataset (not a sample and a population). The two samples vary widely in their size.

Z = \frac{\mu_{pop} - \mu_{sample}}{\sigma / \sqrt{N}}

```
u_total = df['date'][df['User Type'] == 1].groupby([df['date'].dt.weekday]).count()
c_total = df['date'][df['User Type'] == 0].groupby([df['date'].dt.weekday]).count()

u_total = u_total.values
c_total = c_total.values

print(u_total)
print(c_total)
```
[ 91567  93520 130758 134052 114035  61836  74697]

[2388  752 3038 3102 2521 3854 7363]

```
import scipy.stats
scipy.stats.ttest_ind(u_total,c_total)
```
Ttest_indResult(statistic=9.3112138042622536, pvalue=7.6996974734088575e-07)

### Conclution
#### Receiving these results of calculated t-statistic and the extremely small p-value, referring to the very further tail of the distribution, I can reject the Null hypothesis.
