x <- 10
y <- 5

# Perform arithmetic operations
addition <- x + y
subtraction <- x - y
multiplication <- x * y
division <- x / y

#comparison operators
n1 <- 8
n2 <- 9
n3 <- n1 > n2

#logical operators
b1 <- 9
b2 <- 0
b3 <- b1 | b2

b1 <- 8
b2 <- 1
b3 <- !((b1 + b2) < (b1 * b2))

# Print the results
cat("x + y =", addition, "\n")
cat("x - y =", subtraction, "\n")
cat("x * y =", multiplication, "\n")
cat("x / y =", division, "\n")