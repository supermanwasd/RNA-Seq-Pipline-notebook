#1.input_count 2.out_put name
args <- commandArgs(trailingOnly = TRUE)
rawDat <- read.table(args[1],header = T,sep = "\t",stringsAsFactors = F)


co = length(rawDat[1,])
sum_rpk <- apply(rawDat[,7:co],2,sum)

for(i in 7:co){
  rawDat[,i] <- rawDat[,i]/rawDat$Length
}

for(i in 7:co){
  rawDat[,i] <- rawDat[,i]/sum_rpk[i-6]
}

for(i in 7:co){
  rawDat[,i] <- rawDat[,i]*1000000000
}

normDat <- rawDat[,c(1,7:co)]


write.csv(normDat,file = args[2],quote = FALSE,row.names = FALSE)