# Writing data to the file
data = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(data + "\n")
file.close()
print("Data successfully written to output.txt.")

# Appending additional data to the file
extra_data = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(extra_data + "\n")
file.close()
print("Data successfully appended.")

# Reading and displaying the final content
file = open("output.txt", "r")
print("\nFinal content of output.txt:")
print(file.read())
file.close()
