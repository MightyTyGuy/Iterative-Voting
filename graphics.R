res = read.table('results.txt', header = TRUE)
meta = read.table('meta.txt', header = TRUE)

library(RColorBrewer)

makePlot <- function(res, meta, iterations = 300, type = "borda",
                     util = "exp_util", cand = 7, gen = "polya_eggenberger",
                     ylim = c(.7, 1), title = ""){
  
  exp = meta[meta$UtilType == util & 
                meta$Candidates == cand & 
                meta$GenType == gen, ]
  tempres = res[res$ExpNum == exp$ExpNum,]
  
  cols = brewer.pal(9, "Set1")
  if(type == "borda"){
    par(xpd = TRUE)
    plot(rep(exp$Borda_borda, iterations), type = "l", lwd = 3, col = cols[1],
         ylim = ylim, xlab = "Iteration", ylab = "Avg Borda Ratio", main = title)
    lines(rep(exp$Borda_copeland, iterations), lwd = 3, col = cols[2])
    lines(rep(exp$Borda_plurality, iterations), lwd = 3, col = cols[3])
    lines(rep(exp$Borda_stv, iterations), lwd = 3, col = cols[4])
    lines(tempres$Borda_Learning[1:iterations], lwd = 3, col = cols[5])
    lines(tempres$Borda_BestResponse[1:iterations], lwd = 3, col = cols[6])
    lines(tempres$Borda_LearningBayesian[1:iterations], lwd = 3, col = cols[7])
    lines(tempres$Borda_LearningBestResponse[1:iterations], lwd = 3, col = cols[8])
    lines(tempres$Borda_Pragmatist[1:iterations], lwd = 3, col = cols[9])
    legend("topright", inset=c(-0.05,0), legend=c("Borda","Copeland","Plurality",
                                                  "STV", "Learning", "BR",
                                                  "Bayesian", "Learning BR",
                                                  "Pragmatist"), lty = 1, lwd = 3, col = cols)
  }else{
    par(xpd = TRUE)
    plot(rep(exp$Cond_borda, iterations), type = "l", lwd = 3, col = cols[1],
         ylim = ylim, xlab = "Iteration", ylab = "Condorcet Efficiency", main = title)
    lines(rep(exp$Cond_copeland, iterations), lwd = 3, col = cols[2])
    lines(rep(exp$Cond_plurality, iterations), lwd = 3, col = cols[3])
    lines(rep(exp$Cond_stv, iterations), lwd = 3, col = cols[4])
    lines(tempres$Cond_Learning[1:iterations], lwd = 3, col = cols[5])
    lines(tempres$Cond_BestResponse[1:iterations], lwd = 3, col = cols[6])
    lines(tempres$Cond_LearningBayesian[1:iterations], lwd = 3, col = cols[7])
    lines(tempres$Cond_LearningBestResponse[1:iterations], lwd = 3, col = cols[8])
    lines(tempres$Cond_Pragmatist[1:iterations], lwd = 3, col = cols[9])
    legend("topright", inset=c(-0.05,0), legend=c("Borda","Copeland","Plurality",
                                                 "STV", "Learning", "BR",
                                                 "Bayesian", "Learning BR",
                                                 "Pragmatist"), lty = 1, lwd = 3, col = cols)
  }
}

#This is the plot from the paper
#graphic one
makePlot(res, meta, ylim = c(.9,1), title = "Borda Ratio - Exp Util")
#graphic two
makePlot(res, meta, type = "cond", title = "Condorcet Eff - Exp Util")

#same thing with linear util
#graph 3
makePlot(res, meta, ylim = c(.9,1), util = "linear_util", title = "Borda Ratio - Lin Util")
#graph 4
makePlot(res, meta, type = "cond", util = "linear_util", title = "Condorcet Eff - Lin Util")
#graph 5
makePlot(res, meta, type = "cond", util = "linear_util", iterations = 50, title = "Condorcet Eff - Lin Util")

makePlot(res, meta, ylim = c(.9,1), util = "log_util", title = "Borda Ratio - Log Util")
makePlot(res, meta, type = "cond", util = "log_util", ylim = c(.65, 1), title = "Condorcet Eff - Log Util")
makePlot(res, meta, type = "cond", util = "log_util", ylim = c(.65, 1), iterations = 50, title = "Condorcet Eff - Log Util")

makePlot(res, meta, ylim = c(.96,1), cand = 3, util = "linear_util", title = "Borda Ratio - Exp Util")
makePlot(res, meta, ylim = c(.82, 1), type = "cond", util = "linear_util", cand = 3, title = "Condorcet Eff - Exp Util")

makePlot(res, meta, ylim = c(.96,1), cand = 3, util = "log_util", title = "Borda Ratio - Exp Util")
makePlot(res, meta, ylim = c(.82, 1), type = "cond", util = "log_util", cand = 3, title = "Condorcet Eff - Exp Util")

makePlot(res, meta, gen = "impartial_culture", type = "cond", ylim = c(.45, 1))
makePlot(res, meta, gen = "impartial_culture", type = "borda", util = "linear_util", ylim = c(.9, 1))