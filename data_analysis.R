res = read.table('results.txt', header = TRUE)
meta = read.table('meta.txt', header = TRUE)


#compare agent types
comparePlot <- function(res, meta, type = "Borda", util = "exp_util", gen = "polya_eggenberger", cand = 10, iterations = 500){
  
  LA_ex = meta[meta$UtilType == util & meta$GenType == gen & meta$AgentType == "LearningAgent" & meta$Candidates == cand,]$ExpNum
  LR_ex = meta[meta$UtilType == util & meta$GenType == gen & meta$AgentType == "LearningBestResponseAgent" & meta$Candidates == cand,]$ExpNum
  BR_ex = meta[meta$UtilType == util & meta$GenType == gen & meta$AgentType == "BestResponseAgent" & meta$Candidates == cand,]$ExpNum
  PA_ex = meta[meta$UtilType == util & meta$GenType == gen & meta$AgentType == "PragmatistAgent" & meta$Candidates == cand,]$ExpNum
  LB_ex = meta[meta$UtilType == util & meta$GenType == gen & meta$AgentType == "LearningBayesianAgent",]$ExpNum
  if (type == "Borda"){
    LA_1 = res[res$ExpNum == LA_ex & res$Iter < iterations,]$Borda
    #LA_2 = res[res$ExpNum == LA_ex[2],]$Borda
    LR_1 = res[res$ExpNum == LR_ex & res$Iter < iterations,]$Borda
    #LR_2 = res[res$ExpNum == LR_ex[2],]$Borda
    BR_1 = res[res$ExpNum == BR_ex & res$Iter < iterations,]$Borda
    #BR_2 = res[res$ExpNum == BR_ex[2],]$Borda
    PA_1 = res[res$ExpNum == PA_ex & res$Iter < iterations,]$Borda
    #PA_2 = res[res$ExpNum == PA_ex[2],]$Borda
    LB_1 = res[res$ExpNum == LB_ex & res$Iter < iterations,]$Borda
    #LB_2 = res[res$ExpNum == LB_ex[2],]$Borda
    all = c(LA_ex, LR_ex, BR_ex, PA_ex)
    borda = rep(mean(meta[meta$ExpNum %in% all,]$Borda_borda),iterations)
    cope = rep(mean(meta[meta$ExpNum %in% all,]$Borda_copeland),iterations)
    plur = rep(mean(meta[meta$ExpNum %in% all,]$Borda_plurality),iterations)
    stv = rep(mean(meta[meta$ExpNum %in% all,]$Borda_stv),iterations)
    y = "Avg Borda Ratio"
  }
  else{
    LA_1 = res[res$ExpNum == LA_ex & res$Iter < iterations,]$Cond
    #LA_2 = res[res$ExpNum == LA_ex[2],]$Borda
    LR_1 = res[res$ExpNum == LR_ex & res$Iter < iterations,]$Cond
    #LR_2 = res[res$ExpNum == LR_ex[2],]$Borda
    BR_1 = res[res$ExpNum == BR_ex & res$Iter < iterations,]$Cond
    #BR_2 = res[res$ExpNum == BR_ex[2],]$Borda
    PA_1 = res[res$ExpNum == PA_ex & res$Iter < iterations,]$Cond
    #PA_2 = res[res$ExpNum == PA_ex[2],]$Borda
    LB_1 = res[res$ExpNum == LB_ex[1] & res$Iter < iterations,]$Borda
    #LB_2 = res[res$ExpNum == LB_ex[2],]$Borda
    all = c(LA_ex, LR_ex, BR_ex, PA_ex)
    borda = rep(mean(meta[meta$ExpNum %in% all,]$Cond_borda),iterations)
    cope = rep(mean(meta[meta$ExpNum %in% all,]$Cond_copeland),iterations)
    plur = rep(mean(meta[meta$ExpNum %in% all,]$Cond_plurality),iterations)
    stv = rep(mean(meta[meta$ExpNum %in% all,]$Cond_stv),iterations)
    y = "Condorcet Efficiency"
  }
  
  cols = brewer.pal(9, "Set1")
  plot(LA_1, col = cols[1],ylim = c(.6,1), xlab = "Iteration", ylab = y)
  lines(LA_1, col = cols[1])
  points(LB_1, col = cols[2])
  lines(LB_1, col = cols[2])
  points(LR_1, col = cols[3])
  lines(LR_1, col = cols[3])
  points(BR_1, col = cols[4])
  lines(BR_1, col = cols[4])
  points(PA_1, col = cols[5])
  lines(PA_1, col = cols[5])
  points(cope, col = cols[6])
  lines(cope, col = cols[6])
  points(plur, col = cols[7])
  lines(plur, col = cols[7])
  points(stv, col = cols[8])
  lines(stv, col = cols[8])
  points(borda, col = cols[9])
}