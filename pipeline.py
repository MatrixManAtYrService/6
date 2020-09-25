import conducto as co

def go() -> co.Serial:
    with co.Serial() as node:
        co.Exec("echo hi", name='node')
    return node

if __name__ == "__main__":
    co.main(default=go)
