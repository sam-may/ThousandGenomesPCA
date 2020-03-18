import allel

print allel.__version__

with open("data/ALL.chrY.phase3_integrated_v2a.20130502.genotypes.vcf", "r") as f_in:
    data = allel.read_vcf(f_in)

for key, info in data.iteritems():
    print "Key: ", key
    print "Info: ", info.shape
