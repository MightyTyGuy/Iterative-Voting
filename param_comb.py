from experiment import experiment
import agent
import generators

meta_file_name = "meta.txt"
res_file_name = "results.txt"

with open(meta_file_name, 'w') as meta_file:
    with open(res_file_name, 'w') as res_file:
        #add column labels to files (these will be set up like a csv)
        meta_file.write("ExpNum " + "UtilType " + "GenType " + "Alpha " + "Voters " \
                        + "Candidates " + "Iterations " + "Borda_borda " \
                        + "Borda_copeland " + "Borda_plurality " + "Borda_stv " \
                        + "Cond_borda " + "Cond_copeland " \
                        + "Cond_plurality " + "Cond_stv\n")

        res_file.write("ExpNum " + "Iter " + "Borda_Learning " + "Cond_Learning " \
                        + "Borda_BestResponse " + "Cond_BestResponse " \
                        + "Borda_LearningBayesian " + "Cond_LearningBayesian " \
                        + "Borda_LearningBestResponse " + "Cond_LearningBestResponse " \
                        + "Borda_Pragmatist " + "Cond_Pragmatist\n")

num_reps = 1000
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
                print("Current Params:", (util.__name__, gen.__name__, num_cands, num_voters))

                # Create variables for experiment data
                borda_avg = [{'learn': 0, 'bestres': 0, 'bayes': 0, 'learnbr': 0, 'prag': 0} for _ in range(num_iters)]
                cond_avg = [{'learn': 0, 'bestres': 0, 'bayes': 0, 'learnbr': 0, 'prag': 0} for _ in range(num_iters)]

                meta_borda_avg = {'borda': 0, 'plur': 0, 'cope': 0, 'stv': 0}
                meta_cond_avg = {'borda': 0, 'plur': 0, 'cope': 0, 'stv': 0}

                cond_counter = 0

                # Run each repetition
                for rep in range(num_reps):
                    exp = experiment(util, gen, num_cands, num_voters, num_iters, alpha)
                    isCond = exp._isCond

                    # Collect experiment data
                    static_borda, static_cond = exp.getStaticResults()
                    iter_borda, iter_cond = exp.run()

                    # Compute running averages
                    # Borda Ratio
                    for elec_type in static_borda:
                        meta_borda_avg[elec_type] = (1 / (rep + 1)) * (rep * meta_borda_avg[elec_type] + static_borda[elec_type])
                    for i in range(num_iters):
                        for agent_type in iter_borda[i]:
                            borda_avg[i][agent_type] = (1 / (rep + 1)) * (rep * borda_avg[i][agent_type] + iter_borda[i][agent_type])

                    # Condorcet Efficiency
                    if isCond:
                        for elec_type in static_cond:
                            meta_cond_avg[elec_type] = (1 / (cond_counter + 1)) * (cond_counter * meta_cond_avg[elec_type] + static_cond[elec_type])
                        for i in range(num_iters):
                            for agent_type in iter_cond[i]:
                                cond_avg[i][agent_type] = (1 / (cond_counter + 1)) * (cond_counter * cond_avg[i][agent_type] + iter_cond[i][agent_type])
                        cond_counter += 1

                    # Progress
                    if (rep + 1) % 100 == 0:
                        print("Repetition", str(rep+1), "/", str(num_reps))
                
                # Write data to file
                with open(meta_file_name, 'a') as meta:
                    meta.write(str(exp_num) + " " +  util.__name__ + \
                       " " + gen.__name__ + " " + str(alpha) + " " + \
                       str(num_voters) + " " + str(num_cands) + " " + str(num_iters) + " " + \
                       str(meta_borda_avg['borda']) + " " + str(meta_borda_avg['cope']) + " " + str(meta_borda_avg['plur']) + \
                       " " + str(meta_borda_avg['stv']) + " " + str(meta_cond_avg['borda']) \
                       + " " + str(meta_cond_avg['cope']) + " " + str(meta_cond_avg['plur']) + " " + \
                       str(meta_cond_avg['stv']) + "\n")

                with open(res_file_name, 'a') as res:
                    for i in range(num_iters):
                        res.write(str(exp_num) + " " + str(i) + " " + \
                                str(borda_avg[i]['learn']) + " " + str(cond_avg[i]['learn']) + " " + \
                                str(borda_avg[i]['bestres']) + " " + str(cond_avg[i]['bestres']) + " " + \
                                str(borda_avg[i]['bayes']) + " " + str(cond_avg[i]['bayes']) + " " + \
                                str(borda_avg[i]['learnbr']) + " " + str(cond_avg[i]['learnbr']) + " " + \
                                str(borda_avg[i]['prag']) + " " + str(cond_avg[i]['prag']) + "\n")
                
                # Progress
                print("Completed", exp_num, "/", num_combs, "Experiments")