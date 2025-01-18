import hashlib

# Store the hash files function
def hash_file(file1, file2):
    hash1 = hashlib.sha1()
    hash2 = hashlib.sha1()
    
    # Use file.read() to read the size of file 
    # and read the file in small chunks 
    with open(file1, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash1.update(chunk)

    with open(file2, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash2.update(chunk)
    # hexdigest() is of 160 bits 
    return hash1.hexdigest(), hash2.hexdigest()

#Test 1
f1, f2 = hash_file(r"C:\Users\clair\OneDrive\Desktop\Python-Projects\Beginner-Projects\PDF-Check\Test1\The Town Mouse.pdf", r"C:\Users\clair\OneDrive\Desktop\Python-Projects\Beginner-Projects\PDF-Check\Test1\The Town Mouse - Copy.pdf")
#Test 2
f1, f2 = hash_file(r"C:\Users\clair\OneDrive\Desktop\Python-Projects\Beginner-Projects\PDF-Check\Test2\The Lion & the Ass.pdf", r"C:\Users\clair\OneDrive\Desktop\Python-Projects\Beginner-Projects\PDF-Check\Test2\The Lion & the Mouse.pdf")

# Function to compare the hashes and return a message if they are identical or different.
def compare_hashes(hash1, hash2):
    if hash1 == hash2:
        return "The files are identical."
    else:
        return "The files are different."

print(compare_hashes(f1, f2))
