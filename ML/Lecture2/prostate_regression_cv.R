#Load the data
data = read.table('prostate.data.txt',header=TRUE)
# lcavol: Log cancer volume
# lweight: Log prostate weight
# age: Age
# lbph: Log amount benine prostatic hyperplasia
# svi: Seminal vesicle invasion
# lcp: Log capsular penetration
# gleason: Gleason score
# pgg45: percent of Gleason scores 4 or 5

names(data)

#Build train and test data sets
train = data[which(data$train),-10]
test = data[which(!data$train),-10]

#Let's just fit a linear regression
#If we have a data frame, we can just do this with the data frame
fit1 = lm(lpsa ~ ., data=train)
fit1
fit1$coefficients

#If we want predictions and have a data frame, we can use predict
yhat_ls = predict(fit1, newdata=test)
mean((yhat_ls-y_test)^2)

#glmnet can only take matrices, not data frames.  We can convert them like this.
#We are dropping column 9 from X because it is the response, lpsa
X_train = as.matrix(train[,-9])
X_test = as.matrix(test[,-9])
y_train = train$lpsa
y_test = test$lpsa


#### RIDGE REGRESSION ####
#What about Ridge regression?
#We will use glmnet package
#install.packages('glmnet')
library(glmnet)

#Main function glmnet fits things.
?glmnet
#For ridge regression, set alpha = 0
#For regression, choose family='gaussian'
fit_ridge = glmnet(X_train,y_train,family='gaussian',alpha=0)

names(fit_ridge)
#Fits ridge over a range of lambda values
fit_ridge$lambda

#We can plot the coefficients over the range:
plot(fit_ridge,xvar='lambda')

#Extract coefficients at lambda=.2
coef(fit_ridge,s=.2)
#Compute the predictions on new data using beta at lambda=.2
yhat_ridge = predict(fit_ridge,newx=X_test,s=.2)
#Check error: We improve!
mean((yhat_ridge-y_test)^2)
mean((predict(fit_ridge,newx=X_train,s=.2)-y_train)^2)



#### LASSO ####

#Let's fit the lasso.  Almost everything is the same!
#For lasso, set alpha = 1
#For regression, choose family='gaussian'
fit_lasso = glmnet(X_train,y_train,family='gaussian',alpha=1)

#Fits ridge over a range of lambda values
fit_lasso$lambda

#We can plot the coefficients over the range:
plot(fit_lasso,xvar='lambda')

#Extract coefficients at lambda=.1
coef(fit_lasso,s=.1)
#Compute the predictions on new data using beta at lambda=.2
yhat_lasso = predict(fit_lasso,newx=X_test,s=.1)
#Check error: We improve!
mean((yhat_lasso-y_test)^2)



##How did we know to pick s=.1?
##Let's do CV?  (Note, this works for ridge too)

#We use cv.glmnet
?cv.glmnet
#The syntax is almost the same!
cv_lasso = cv.glmnet(X_train,y_train,family='gaussian',alpha=1)
names(cv_lasso)

#Plot the average cv error
plot(cv_lasso)

#We can pull out the mean, sd, upper, and lower bounds with
cv_lasso$cvm
cv_lasso$cvup
cv_lasso$cvlo
#so we can make pretty custom plots, like
plot(log(cv_lasso$lambda),cv_lasso$cvm,ylim=c(min(cv_lasso$cvlo),max(cv_lasso$cvup)),type='l')
polygon(c(log(cv_lasso$lambda),rev(log(cv_lasso$lambda))),c(cv_lasso$cvup,rev(cv_lasso$cvlo)),col='grey',border=NA)
lines(log(cv_lasso$lambda),cv_lasso$cvm)

#we can also directly access the chosen values of lambda
cv_lasso$lambda.min
cv_lasso$lambda.1se

#We can check the estimated prediction error from the cv
idx_min = which(cv_lasso$lambda==cv_lasso$lambda.min)
idx_1se = which(cv_lasso$lambda==cv_lasso$lambda.1se)
cv_lasso$cvm[idx_min]
cv_lasso$cvm[idx_1se]
cv_lasso$cvlo[idx_min]
cv_lasso$cvlo[idx_1se]


#And we can check the prediction error for each
mean((predict(fit_lasso,newx=X_test,s=cv_lasso$lambda.min)-y_test)^2)
#The min lambda does about as well as ridge regression
mean((predict(fit_lasso,newx=X_test,s=cv_lasso$lambda.1se)-y_test)^2)
#The -1se lambda beats it!  And it's more interpretable!
coef(fit_lasso,s=cv_lasso$lambda.min)
coef(fit_lasso,s=cv_lasso$lambda.1se)


