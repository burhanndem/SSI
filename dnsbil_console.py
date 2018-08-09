from dnsibl import Mhs

class Console:

    def run(self):
        print("\nWelcome to SSI v.0.0.1!!\n")
        site=input("\nWhich site do you want to get information about ? : ")
        print("\n\n")
        ornk=Mhs()
        ornk.hubele(site)



if __name__ == '__main__':
        c=Console()
        c.run()