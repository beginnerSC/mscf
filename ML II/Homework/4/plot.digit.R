
plot.digit = function(x,zlim=c(-1,1)) {
  x = as.matrix(x)
  cols = gray.colors(100)[100:1]
  image(matrix(x,nrow=16)[,16:1],col=cols,
        zlim=zlim,axes=FALSE)  
}
