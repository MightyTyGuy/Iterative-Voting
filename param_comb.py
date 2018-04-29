from experiment import experiment
import agent
import generators

meta_file_name = "meta.txt"
res_file_name = "results.txt"
meta_file = open(meta_file_name, 'w')
res_file = open(res_file_name, 'w')

#add column labels to files (these will be set up like a csv)
meta_file.write("ExpNum " + "ExpRep " + "UtilType " + "GenType " + "Alpha " + "Voters " \
                   + "Candidates " + "Iterations " + "Borda_borda " \
                   + "Borda_copeland " + "Borda_plurality " + "Borda_stv " \
                   + "Condorcet " + "Cond_borda " + "Cond_copeland " \
                   + "Cond_plurality " + "Cond_stv\n")

res_file.write("ExpNum " + "ExpRep " + "Iter " + "Borda_Learning " + "Cond_Learning " \
                   + "Borda_BestResponse " + "Cond_BestResponse " \
                   + "Borda_LearningBayesian " + "Cond_LearningBayesian " \
                   + "Borda_LearningBestResponse " + "Cond_LearningBestResponse" \
                   + "Borda_Pragmatist" + "Cond_Pragmatist\n")

meta_file.close()
res_file.close()

num_reps = 100
num_iters = 400
alpha = 0.1
gens = [generators.impartial_culture, generators.polya_eggenberger]
utils = [agent.linear_util, agent.exp_util, agent.log_util]
cands = [7, 3]
voters = [9]

num_combs = len(utils) * len(gens) * len(voters) * len(cands)

exp_num = 0

for util in utils:
    for gen in gens:
        for num_voters in voters:
            for num_cands in cands:
                exp_num += 1
                print("Current Params:", (util, gen, num_voters, num_cands))
                for rep in range(num_reps):
                    experiment(util, gen, num_voters, num_cands, exp_num, \
                    rep, meta_file_name, res_file_name, num_iters, alpha)
                print("Completed", exp_num, "/", num_combs, "Experiments")