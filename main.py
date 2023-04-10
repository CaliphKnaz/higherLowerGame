from gameData import data
import random


def randomAccount():
    account = random.randint(1, 49)
    return data[account]


def compareAccounts(account, account2):
    print(
        f"{account['name']}, a {account['description']} , from {account['country']}")
    print(
        f"{account2['name']}, a {account2['description']} , from {account2['country']}")

    if account["follower_count"] > account2["follower_count"]:
        # print(f" {account['name']} has a larger follower account")
        print("A")
        return account
    else:
        # print(f" {account2['name']} has a larger follower account")
        print("B")
        return account2


def userChoice(account, account2):
    continue_game = True
    while continue_game:
        result = compareAccounts(account, account2)
        if result == account2:
            answer = "B"
        else:
            answer = "A"

        choice = input(
            "Which account has a higher following?. \n 'A' or 'B'").upper()

        if choice == answer:
            global score_counter
            score_counter += 1

            print(score_counter)
            print("Correct")
            account2 = randomAccount()
            userChoice(account=result, account2=account2)

            return True
        else:
            print(f"That was incorrect \n Final score was {score_counter} ")
            continue_game = False
            return False


score_counter = int()
account = randomAccount()
account2 = randomAccount()
# continue_game = True
verdict = userChoice(account=account, account2=account2)
