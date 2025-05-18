# Create a file and write data to it
f = open("file1.txt", "w+")  # Corrected the file extension to .txt
f.write("hello world")       # Corrected the spelling of "hello"
f.seek(0)                    # Move the cursor to the beginning of the file to read from it
print(f.read())              # Read and print the content of the file
f.close()                    # Close the file
