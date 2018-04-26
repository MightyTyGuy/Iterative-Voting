from experiment_group import experiment_group
import agent
import generators

tests = []

meta_file_name = "meta.txt"
res_file_name = "results.txt"
meta_file = open(meta_file_name, 'w')
res_file = open(res_file_name, 'w')

#add column labels to files (these will be set up like a csv)
meta_file.write("ExpNum " + "AgentType " + "UtilType " + "GenType " + "Alpha " + "Voters " + "Candidates " + "Iterations " + "Experiments " + "Borda_borda " \
                   + "Borda_copeland " + "Borda_plurality " + "Borda_stv " + "Condorcet " + "Cond_borda " + "Cond_copeland " + "Cond_plurality " \
                   + "Cond_stv\n")

res_file.write("ExpNum " + "Iter " + "Borda " + "Cond\n")

meta_file.close()
res_file.close()

tests.append(experiment_group(agent.BestResponseAgent, agent.linear_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 1))
tests.append(experiment_group(agent.BestResponseAgent, agent.linear_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 2))
tests.append(experiment_group(agent.BestResponseAgent, agent.exp_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 3))
tests.append(experiment_group(agent.BestResponseAgent, agent.exp_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 4))
tests.append(experiment_group(agent.BestResponseAgent, agent.log_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 5))
tests.append(experiment_group(agent.BestResponseAgent, agent.log_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 6))
tests.append(experiment_group(agent.BestResponseAgent, agent.linear_util, generators.polya_eggenberger, 100, 10, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 13))
tests.append(experiment_group(agent.BestResponseAgent, agent.linear_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 14))
tests.append(experiment_group(agent.BestResponseAgent, agent.exp_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 15))
tests.append(experiment_group(agent.BestResponseAgent, agent.exp_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 16))
tests.append(experiment_group(agent.BestResponseAgent, agent.log_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 17))
tests.append(experiment_group(agent.BestResponseAgent, agent.log_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 18))

tests.append(experiment_group(agent.PragmatistAgent, agent.linear_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 25))
tests.append(experiment_group(agent.PragmatistAgent, agent.linear_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 26))
tests.append(experiment_group(agent.PragmatistAgent, agent.exp_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 27))
tests.append(experiment_group(agent.PragmatistAgent, agent.exp_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 28))
tests.append(experiment_group(agent.PragmatistAgent, agent.log_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 29))
tests.append(experiment_group(agent.PragmatistAgent, agent.log_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 30))
tests.append(experiment_group(agent.PragmatistAgent, agent.linear_util, generators.polya_eggenberger, 100, 10, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 37))
tests.append(experiment_group(agent.PragmatistAgent, agent.linear_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 38))
tests.append(experiment_group(agent.PragmatistAgent, agent.exp_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 39))
tests.append(experiment_group(agent.PragmatistAgent, agent.exp_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 40))
tests.append(experiment_group(agent.PragmatistAgent, agent.log_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 41))
tests.append(experiment_group(agent.PragmatistAgent, agent.log_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 42))

tests.append(experiment_group(agent.LearningAgent, agent.linear_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 49))
tests.append(experiment_group(agent.LearningAgent, agent.linear_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 50))
tests.append(experiment_group(agent.LearningAgent, agent.exp_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 51))
tests.append(experiment_group(agent.LearningAgent, agent.exp_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 52))
tests.append(experiment_group(agent.LearningAgent, agent.log_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 53))
tests.append(experiment_group(agent.LearningAgent, agent.log_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 54))
tests.append(experiment_group(agent.LearningAgent, agent.linear_util, generators.polya_eggenberger, 100, 10, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 61))
tests.append(experiment_group(agent.LearningAgent, agent.linear_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 62))
tests.append(experiment_group(agent.LearningAgent, agent.exp_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 63))
tests.append(experiment_group(agent.LearningAgent, agent.exp_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 64))
tests.append(experiment_group(agent.LearningAgent, agent.log_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 65))
tests.append(experiment_group(agent.LearningAgent, agent.log_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 66))

tests.append(experiment_group(agent.LearningBestResponseAgent, agent.linear_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 73))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.linear_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 74))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.exp_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 75))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.exp_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 76))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.log_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 77))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.log_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 78))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.linear_util, generators.polya_eggenberger, 100, 10, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 85))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.linear_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 86))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.exp_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 87))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.exp_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 88))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.log_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 89))
tests.append(experiment_group(agent.LearningBestResponseAgent, agent.log_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 90))

tests.append(experiment_group(agent.LearningBayesianAgent, agent.linear_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 91))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.linear_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 92))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.exp_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 93))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.exp_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 94))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.log_util, generators.impartial_culture, 100, 10, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 95))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.log_util, generators.impartial_culture, 100, 3, 500, 100, alpha = None, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 96))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.linear_util, generators.polya_eggenberger, 100, 10, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 97))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.linear_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 98))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.exp_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 99))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.exp_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 100))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.log_util, generators.polya_eggenberger, 100, 10, 500,100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 101))
tests.append(experiment_group(agent.LearningBayesianAgent, agent.log_util, generators.polya_eggenberger, 100, 3, 500, 100, .1, write = True, meta_file = "meta.txt", results_file = "results.txt", exp_num = 102))
