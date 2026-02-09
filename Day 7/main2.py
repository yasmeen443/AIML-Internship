try:
    file=open("example3.txt","r")
    print(file.read())
except Exception as e:
    print(f"Error:{e}")

finally:
    print("file not found")