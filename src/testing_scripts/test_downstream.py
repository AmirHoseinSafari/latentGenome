import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import re

'''
pe_int_path = "/opt/data/latent/data/downstream/PE-interactions"
nonpredictors = ['enhancer_chrom', 'enhancer_start', 'enhancer_end', 'promoter_chrom', 'promoter_start', 'promoter_end',
                 'window_chrom', 'window_start', 'window_end', 'window_name', 'active_promoters_in_window',
                 'interactions_in_window', 'enhancer_distance_to_promoter', 'bin', 'label']

training_df = pd.read_hdf(pe_int_path + '/training.h5', 'training').set_index(['enhancer_name', 'promoter_name'])
predictors_df = training_df.drop(nonpredictors, axis=1)
labels = training_df['label']

estimator = GradientBoostingClassifier(n_estimators=20, learning_rate=0.1, max_depth=2, max_features='log2',
                                       random_state=0)

estimator.fit(predictors_df, labels)
importances = pd.Series(estimator.feature_importances_, index=predictors_df.columns).sort_values(ascending=False)
print(importances.head(16))
'''

'''
# read wiggle file 
rex = re.compile('fixedStep chrom=(\S+) start=(\d+) step=(\d+)')

dir_path = "/data2/latent/data/interpretation/phylogenetic_scores/"
chr_21_length = 46, 709, 983
p_score = np.zeros((48119900, 1))

file_path = dir_path + "chr21.phyloP100way.wigFix"

start = 0
count = 0

f = open(file_path)
for line in f:
    if line.startswith('fixedStep'):
        m = rex.match(line.strip())
        if m is None:
            raise (Exception, "Not a valid fixedStep line:\n{0}\nAbort!!".format(line))

        chr = m.group(1)
        start = int(m.group(2))
        step = int(m.group(3))

        count = 0
    else:
        score = float(line.strip())
        p_score[start + count] = score
        count += 1

np.save(dir_path + "p_score.npy", p_score)

'''

'''
dir_path = "/data2/latent/data/interpretation/phylogenetic_scores/"
npy_path = dir_path + "p_score.npy"

p_score = np.load(npy_path)
window = 25
reduced_p_score = np.zeros((int(len(p_score) / window), 1))
count = 0

for cut in range(int(len(p_score)/window)):
    reduced_p_score[count] = p_score[cut * window: (cut + 1) * window].mean()
    count += 1

print("done")
'''

# gene_windows = "/home/kevindsouza/Documents/projects/latentGenome/results/04-27-2019_n/h_110/5e-14/21/rna_windows.pkl"
# pe_windows = "/home/kevindsouza/Documents/projects/latentGenome/results/04-27-2019_n/h_110/5e-14/21/pe_windows.pkl"
# chr_21 = "/home/kevindsouza/Documents/projects/latentGenome/results/04-27-2019_n/h_110/5e-14/21/feat_chr_21.pkl"
# phylo = "/home/kevindsouza/Documents/projects/latentGenome/results/04-27-2019_n/h_110/5e-14/21/feat_phylo_chr_21.pkl"

'''
gene = pd.read_pickle(gene_windows)
pe = pd.read_pickle(pe_windows)

pe['promoter_middle'] = pd.to_numeric(np.floor(pe['promoter_start'] + (pe['promoter_end'] - pe['promoter_start']) / 2))
pe['enhancer_middle'] = pd.to_numeric(np.ceil(pe['enhancer_start'] + (pe['enhancer_end'] - pe['enhancer_start']) / 2))

pe_middle = pe.filter(['promoter_middle', 'enhancer_middle', 'cell'], axis=1)

genes = gene_windows.loc[(gene_windows['end'] - gene_windows['start']) > 400]
'''
# phylo = pd.read_pickle(phylo)

#p_path = "/home/kevindsouza/Documents/projects/latentGenome/results/06-25-2019_n/h3_ch21/assay/windows/assay_21_promoter_E017"
#e_path = "/data2/latent/data/interpretation/enhancers/enhancers.txt"

#prom = pd.read_pickle(p_path)
#en = pd.read_pickle(e_path)

#assay_path = "/home/kevindsouza/Documents/projects/latentGenome/results/06-25-2019_n/h3_ch21/assay/new_positions/assay_21_promoter.pkl"
#assay = pd.read_pickle(assay_path)

'''
df = pd.read_table(e_path, delim_whitespace=True)
enhancer_positions = df['Id']
enhancer_positions = enhancer_positions.loc[37528:38586].reset_index(drop=True)
'''

'''
chr_21 = "/home/kevindsouza/Documents/projects/latentGenome/results/04-27-2019_n/h_110/5e-14/21/lstm_features/feat_chr_21.pkl"
chr_20 = "/home/kevindsouza/Documents/projects/latentGenome/results/04-27-2019_n/h_110/5e-14/21/lstm_features/feat_chr_20.pkl"

feat_21 = pd.read_pickle(chr_21)
feat_20 = pd.read_pickle(chr_20)
'''

chromosome_path = "/data2/latent/data/avocado/avocado_features/avo_chr_21.pkl"
chromosome = pd.read_pickle(chromosome_path)

print("done")
