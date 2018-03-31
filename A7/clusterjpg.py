import clusters

blognames,words,data=clusters.readfile('/home/tim/Documents/A7/blogdata1.txt')
clust=clusters.hcluster(data)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg') 

