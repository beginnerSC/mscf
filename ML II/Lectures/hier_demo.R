# Simple demo of hierarchical clustering
set.seed(4)
n <- 4
x <- rbind(matrix(rnorm(2*n, sd=0.2), ncol=2),
           scale(matrix(rnorm(2 * n, sd = 0.3), ncol = 2), 
                 center = -c(1, 1), scale=FALSE),
           scale(matrix(rnorm(2 * n, sd = 0.2), ncol = 2),
                 center = -c(0, 1), scale = FALSE))

hier <- hclust(dist(x), method='complete')

plot(x[,1], x[,2], pch = 19)
cols <- c("#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")

# Annoying function to make it easy to color the groups
colmap <- function(v, cols) {
  tab <- table(v)
  nonsingle <- which(table(v) > 1)
  map <- rep(cols[1], length(unique(v)))

  for(i in 1:length(nonsingle)) {
    map[nonsingle[i]] <- cols[i + 1]
  }
  map[v]
}

# Let's loop up the tree, drawing what happens as we merge groups.
# Points in a group all on their own are shown in gray; groups with more
# than one point are shown in color.
par(ask = TRUE)
for(k in 1:(3 * n)) {
  # Extract 3*n-k+1 groups
  v <- cutree(hier, k = (3 * n - k + 1))
  ngroups <- length(unique(v))
  
  print(v)
  
  plot(x[,1], x[,2], pch = 19, col = colmap(v, cols), cex = 2,
       main = paste("Number of groups:", ngroups))  
}
par(ask = FALSE)


# Visualize this as a tree
plot(hier)
