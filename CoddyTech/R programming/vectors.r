#Vectors are one-dimensional arrays that can hold elements of the same data type. 
#Vectors are essential for storing and manipulating collections of data in R.

numeric_vector <- c(1, 2, 3, 4, 5)
character_vector <- c("apple", "banana", "cherry")
logical_vector <- c(TRUE, FALSE, TRUE, TRUE)

sequence_vector <- 1:5  # Creates a vector of integers from 1 to 5

seq_vector <- seq(from = 0, to = 1, by = 0.25)

#Accessing Vector Elements

fruits <- c("apple", "banana", "cherry")
first_fruit <- fruits[1]  # Returns "apple"
second_fruit <- fruits[2]  # Returns "banana"

#Vector Operations

vec1 <- c(1, 2, 3)
vec2 <- c(4, 5, 6)
sum_vec <- vec1 + vec2  # Results in c(5, 7, 9)

vec <- c(1, 2, 3, 4, 5)
vec_length <- length(vec)  # Returns 5

num_vec <- c(1, 2, 3)
char_vec <- c("a", "b", "c")
typeof(num_vec)  # Returns "double"
typeof(char_vec)  # Returns "character"

# Create the temperatures vector
temperatures <- c(22.5, 25.3, 18.9, 20.1, 23.7)
# Placeholder for average temperature
average_temp <- mean(temperatures)
# Placeholder for highest temperature
highest_temp <- max(temperatures)
# Placeholder for lowest temperature
lowest_temp <- min(temperatures)
# Placeholder for temperature range
temp_range <- highest_temp - lowest_temp
# Placeholder for count of temperatures
temp_count <- length(temperatures)

# Print the results
cat("Average:", sprintf("%.1f", average_temp), "\n")
cat("Highest:", highest_temp, "\n")
cat("Lowest:", lowest_temp, "\n")
cat("Range:", sprintf("%.1f", temp_range), "\n")
cat("Count:", temp_count, "\n")