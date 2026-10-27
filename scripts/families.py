# family name -> list of pattern substrings (case-insensitive); first match wins within topic
FAM = {
'CAL': [
 ('Limits, sequences & series', ['riemann','n-th roots','recursive sequence','monotone bounded','positive and negative parts','absolute vs conditional','radius of convergence','power series','countable']),
 ('Continuity, differentiability & uniform continuity', ['uniform continuity','differentiab','continuity: removable','boundedness of a function','partial derivatives and their continuity','continuous functions','mean value','integral equation','integrating factor','monotonicity from convexity','symmetric second difference']),
 ('Maxima, minima & constrained optimisation', ['critical points','extrema','max distance','maximum of xy','closest point','constrained minimum']),
 ('Integration: area, volume, multiple integrals', ['integral','area','volume','green']),
],
'LA': [
 ('Eigenvalues of functions of a matrix (p(A), A⁻¹, powers)', ['polynomial in','eigenvalues of a polynomial','(a+i)','trace of matrix powers','powers of a reflection','spectral decomposition','cayley–hamilton','idempotent','centring matrix','rank-one','i + vv']),
 ('Diagonalizability, minimal polynomial & Jordan form', ['diagonaliz','minimal polynomial','jordan','nilpotent','rotation','so(3)','cayley transform']),
 ('Rank, nullity, subspaces & dimension', ['rank','null','dimension','span','basis','orthogonal complement','invertibility','surjectiv','find a from','solve for a vector','projection','parseval','commuting','determinant multilinearity','skew-symmetric of odd']),
 ('Definite matrices, singular values & quadratic forms', ['positive definite','psd','singular value','rayleigh','lyapunov']),
],
'PROB': [
 ('Independence of events', ['independence']),
 ('Conditional probability & expectation by counting', ['conditional expectation','sequential testing','at least k']),
 ('σ-fields & probability spaces', ['σ-field','countable sample space','geometric distribution: limits']),
],
'RV': [
 ('Reading distributions from CDF / MGF / c.f.', ['cdf','mgf','characteristic function','jump','median from','lattice']),
 ('Transformations & probability integral transform', ['transformation','→ exponential','integral transform','uniform: cauchy','−log u','floor of','probability for a function','pareto']),
 ('Order statistics', ['order statistic','p(min']),
 ('Standard distributions: moments & parameters', ['poisson','beta','gamma','weibull','lognormal','binomial','exponentials','chi-square','geometric','moments','expectation of','existence','density','mixture','symmetry','differences of i.i.d','p(x < cy','random number of variables']),
],
'JD': [
 ('Multinomial distribution', ['multinomial']),
 ('Conditional distributions & regression function', ['conditional','regression (conditional mean)','e(y²) via','hierarchical']),
 ('Recognising joint distributions (MGF / CDF / pmf)', ['read','recognise','normalising']),
 ('Independence vs correlation', ['independ','uncorrelated','pairwise']),
 ('Sums of random variables', ['sum of two']),
],
'LT': [
 ('Borel–Cantelli & almost sure convergence', ['borel','almost sure','escaping mass','modes of convergence','relations among']),
 ('LLN & consistency', ['lln','consistency','slln','variance of sample mean','wlln']),
 ('CLT, delta method & limiting distributions', ['clt','delta','gumbel','extreme value','moments of squares','pointwise limit','shrinking mean','binary expansion']),
 ('Inequalities', ['jensen']),
],
'SP': [
 ('Markov chains: classification & stationary distributions', ['classify','stationary','uniqueness','limiting','long-run','period','periodic','existence of stationary','birth–death stationary']),
 ('Markov chains: n-step & path probabilities', ['distribution at step','path probability','two-step','2-step','conditional on past','hitting']),
 ('Poisson process', ['poisson','competing exponentials','memoryless']),
 ('Brownian motion', ['brownian']),
 ('Birth–death processes & Kolmogorov equations', ['kolmogorov','pure birth']),
],
'EST': [
 ('Maximum likelihood estimation', ['mle']),
 ('Method of moments', ['method of moments']),
 ('Sufficiency, completeness & Basu', ['sufficien','complete','basu','ancillar']),
 ('Unbiasedness, UMVUE, Rao–Blackwell & CRLB', ['unbiased','umvue','lehmann','rao–blackwell','cramér','crlb','mse','consistency','efficient']),
],
'CI': [
 ('Pivots & confidence intervals', ['']),
],
'TH': [
 ('Neyman–Pearson lemma & MP tests', ['np lemma','np test','mp test','simple vs simple']),
 ('UMP tests, MLR & LRT', ['ump','mlr','lrt','likelihood ratio','rao–blackwellised']),
 ('Size, power & p-values', ['size','power','p-value','sample size','type-i']),
 ('Chi-square tests', ['chi-square']),
],
'NP': [
 ('Rank tests: sign, Wilcoxon, Mann–Whitney', ['sign test','wilcoxon','mann–whitney','ranks','order statistics covering']),
 ('Empirical CDF & Kolmogorov–Smirnov', ['empirical','kolmogorov']),
 ('Rank correlation', ['spearman']),
],
'REG': [
 ('Least squares estimates & prediction', ['ols','fit simple','through the origin','through origin','blue','ridge','ls vs mle','identifiability','exact fit','transformed regressor']),
 ('Variances & covariances of estimators', ['variance','correlation of intercept','cov(','unbiased estimate of σ²','joint confidence']),
 ('ANOVA, F-test & R²', ['anova','r²','f test']),
],
'MV': [
 ('Multivariate normal: independence, conditionals & linear forms', ['independence in multivariate','conditional','linear combination','symmetry','e[max','covariance of linear','read covariance','orthant','regression line','expectation/variance','orthogonal transforms','kendall']),
 ('Partial & multiple correlation', ['partial','multiple correlation']),
 ('Quadratic forms, Wishart & Hotelling T²', ['quadratic','wishart','hotelling','cochran','mahalanobis','sample covariance','mle of mean vector']),
 ('PCA, discriminant analysis & clustering', ['principal','pca','lda','fisher','clustering']),
],
'GA': [
 ('Verbal ability: grammar & vocabulary', ['grammar','vocabulary','verbal analogy','sentence ordering']),
 ('Reading comprehension & inference', ['passage']),
 ('Logical reasoning', ['syllogism','puzzle','truth-teller','liar','seating','arrangement','ordering puzzle','coding','letter-position','series']),
 ('Quantitative aptitude', ['percentage','ratio','speed','profit','mixture','sums of','compound','identity','inequalit','permutation','sets','am–gm','logarithm','energy','equations','counting free','mean, median']),
 ('Geometry, spatial & data interpretation', ['mensuration','symmetry','spatial','squares in','coordinate','grid','data interpretation','cube']),
],
'DOE': [
 ('ANOVA degrees of freedom & estimability', ['anova','estimab']),
 ('Factorial designs, confounding & Latin squares', ['confound','latin']),
],
}
def family(topic, pattern):
    p = pattern.lower()
    for name, keys in FAM[topic]:
        if any(k in p for k in keys): return name
    return None
