from manager import PasswordManager

def main():
    manager = PasswordManager()
    
    master_password = input("🔐 Enter Master Password: ")
    manager.authenticate(master_password)
    
    while True:
        print("\n🔒 PASSWORD MANAGER")
        print("1. Add Password")
        print("2. Get Password")
        print("3. List Services")
        print("4. Delete Password")
        print("5. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            service = input("Service: ")
            username = input("Username: ")
            password = input("Password: ")
            manager.add_password(service, username, password)
        elif choice == '2':
            service = input("Service: ")
            manager.get_password(service)
        elif choice == '3':
            manager.list_services()
        elif choice == '4':
            service = input("Service: ")
            manager.delete_password(service)
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
