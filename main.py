from tasks import add

if __name__ == "__main__":
    result = add.delay(20, 30)
    print(result)
    print(result.forget())
    print(result.ready())
