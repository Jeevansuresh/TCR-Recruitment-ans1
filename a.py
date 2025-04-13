from b import *

def main():
    print(add_noise("hello"))

main()

'''
Function not being called – random_noise needs parentheses: random_noise()

Unwanted print on import – top-level code in a Python file runs during import. 
Wrapping with if __name__ == "__main__": prevents this unless the file is run directly.

'''
